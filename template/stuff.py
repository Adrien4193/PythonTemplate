from pydantic import PositiveInt
from pydantic.dataclasses import dataclass


@dataclass
class Stuff:
    a: str
    b: PositiveInt


def run() -> None:
    data = Stuff("test", 1)
    print(f"It works {data}")
