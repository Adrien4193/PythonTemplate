from pydantic import PositiveInt, BaseModel


class Stuff(BaseModel):
    a: str
    b: PositiveInt


def run() -> None:
    data = Stuff(a="test", b=1)
    print(f"It works {data}")
