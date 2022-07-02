import os

from dotenv import load_dotenv
from web3 import Web3
from constants import ERC_165_ABI, ERC_721_ABI, ERC_721_INTERFACE_ID

load_dotenv()

w3 = Web3(Web3.HTTPProvider(os.environ["RPC_URL"]))

current_block = w3.eth.get_block("latest")["number"]
current_contract_address = "0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d"

address = w3.toChecksumAddress(current_contract_address)
contract_erc_165 = w3.eth.contract(address=address, abi=ERC_165_ABI)
contract_erc_721 = w3.eth.contract(address=address, abi=ERC_721_ABI)
supports_721 = contract_erc_165.functions.supportsInterface(ERC_721_INTERFACE_ID).call()


def get_record_from_log(log):
    # Caching needed

    record = {
        "tx_hash": log["transactionHash"],
        "block_number": log["blockNumber"],
        "block_hash": log["blockHash"],
        "contract_address": log["address"],
        "from": log["args"]["from"],
        "to": log["args"]["to"],
        "token_id": log["args"]["tokenId"],
        # "token_name": "N/A",
        # "token_symbol": "N/A",
        # "token_decimal": "N/A",
        "transaction_index": log["transactionIndex"],
        # "cumulative_gas_used": "N/A",
        # "confirmations": "N/A",
        # "from_balance": "N/A",
        # "to_balance": "N/A",
    }

    return get_balance_data(get_block_data(get_transaction_data(record)))


def get_transaction_data(record):
    block_number = record["block_number"]
    transaction_index = record["transaction_index"]

    transaction = w3.eth.get_transaction_by_block(block_number, transaction_index)

    return record | {
        "gas": transaction["gas"],
        "gas_price": transaction["gasPrice"],
        "nonce": transaction["nonce"],
    }


def get_block_data(record):
    block_number = record["block_number"]
    block = w3.eth.get_block(block_number)

    return record | {
        "block_timestamp": block["timestamp"],
        "gas_used": block["gasUsed"],
    }


def get_balance_data(record):
    return record


supports_721 = contract_erc_165.functions.supportsInterface(ERC_721_INTERFACE_ID).call()

if supports_721:
    filter = contract_erc_721.events.Transfer.createFilter(
        fromBlock=12316269, toBlock=12316269 + 2000
    )

    records = [get_record_from_log(entry) for entry in filter.get_all_entries()]
    print(records)
