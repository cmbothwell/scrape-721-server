from enum import Enum


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
