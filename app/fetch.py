import os
import time
import requests
import csv

from typing import Any
from enum import Enum
from dotenv import load_dotenv
from web3 import Web3
from tqdm import tqdm

load_dotenv()

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
CACHE: dict[str, str] = {}

w3 = Web3(Web3.HTTPProvider(os.environ["RPC_URL"]))


class Contract(Enum):
    HASHMASKS = (
        "HASHMASKS",
        "0xC2C747E0F7004F9E8817Db2ca4997657a7746928",
    )
    BAYC = (
        "BAYC",
        "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D",
    )
    MAYC = (
        "MAYC",
        "0x60E4d786628Fea6478F785A6d7e704777c86a7c6",
    )
    COOLCATS = (
        "COOLCATS",
        "0x1A92f7381B9F03921564a437210bB9396471050C",
    )
    MEEBITS = (
        "MEEBITS",
        "0x7Bd29408f11D2bFC23c34f18275bBf23bB716Bc7",
    )
    CYBERKONGZ = (
        "CYBERKONGZ",
        "0x57a204AA1042f6E66DD7730813f4024114d74f37",
    )
    SVS = (
        "SVS",
        "0x219B8aB790dECC32444a6600971c7C3718252539",
    )
    MEKAVERSE = (
        "MEKAVERSE",
        "0x9A534628B4062E123cE7Ee2222ec20B86e16Ca8F",
    )

    def __new__(cls, *args, **kwds):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    # ignore the first param since it's already set by __new__
    def __init__(self, _: str, address: str | None = None):
        self._address_ = address

    def __str__(self):
        return self.value

    # this makes sure that the description is read-only
    @property
    def address(self):
        return self._address_


def fetch(job_hash: str, contract_address: str) -> None:
    transactions: list[Any] = []
    trailing_block: int = 0
    terminus_block: int = w3.eth.get_block("latest")["number"]

    while trailing_block != terminus_block:
        start_block: int = trailing_block
        for page in range(1, 11):
            time.sleep(0.5)
            fresh_transactions = get_page(
                contract_address, page, start_block, terminus_block
            )

            try:
                if not fresh_transactions:
                    trailing_block = terminus_block
                    break

                transactions += fresh_transactions
                trailing_block = fresh_transactions[-1]["blockNumber"]
            except IndexError:
                trailing_block = terminus_block
                break

    transactions_with_balances = [
        add_balance_data(transaction) for transaction in tqdm(transactions)
    ]
    write_file(job_hash, transactions_with_balances)


def get_page(
    contract_address: str, page: int, start_block: int, terminus_block: int
) -> Any:
    print(f"Fetching Page {page} in block {start_block}")
    params: dict[str, str | int] = {
        "module": "account",
        "action": "tokennfttx",
        "contractaddress": contract_address,
        "page": page,
        "offset": 1000,
        "startblock": start_block,
        "endblock": terminus_block,
        "sort": "asc",
        "apikey": os.environ["ETHERSCAN_API_KEY"],
    }

    r = requests.get("https://api.etherscan.io/api", params=params)
    return r.json()["result"]


def add_balance_data(transaction: Any) -> Any:
    # block = transaction["blockNumber"]

    # from_address = Web3.toChecksumAddress(transaction["from"])
    # to_address = Web3.toChecksumAddress(transaction["to"])

    # if from_address in CACHE:
    #     from_balance = CACHE[from_address]
    # else:
    #     from_balance = str(w3.eth.get_balance(from_address))
    #     CACHE[from_address] = from_balance

    # if to_address in CACHE:
    #     to_balance = CACHE[to_address]
    # else:
    #     to_balance = str(w3.eth.get_balance(to_address))
    #     CACHE[to_address] = to_balance

    return {**transaction, "from_balance": 0, "to_balance": 0}


def write_file(job_hash: str, transactions: list[Any]):
    f = csv.writer(open(f"{DIR_PATH}/completed_jobs/{job_hash}.csv", "w+"))

    # Header row -> we use different column names
    f.writerow(
        [
            "tx_hash",
            "block_number",
            "block_timestamp",
            "block_hash",
            "contract_address",
            "from",
            "to",
            "token_id",
            "token_name",
            "token_symbol",
            "token_decimal",
            "transaction_index",
            "gas",
            "gas_used",
            "cumulative_gas_used",
            "gas_price",
            "nonce",
            "confirmations",
            "from_balance",
            "to_balance",
        ]
    )

    for transaction in transactions:
        f.writerow(
            [
                transaction["hash"],
                transaction["blockNumber"],
                transaction["timeStamp"],
                transaction["blockHash"],
                transaction["contractAddress"],
                transaction["from"],
                transaction["to"],
                transaction["tokenID"],
                transaction["tokenName"],
                transaction["tokenSymbol"],
                transaction["tokenDecimal"],
                transaction["transactionIndex"],
                transaction["gas"],
                transaction["gasUsed"],
                transaction["cumulativeGasUsed"],
                transaction["gasPrice"],
                transaction["nonce"],
                transaction["confirmations"],
                transaction["from_balance"],
                transaction["to_balance"],
            ]
        )


if __name__ == "__main__":
    fetch("TEST", Contract.MEKAVERSE.address)
