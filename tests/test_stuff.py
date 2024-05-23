import pytest

from template import Stuff


def test_ok() -> None:
    Stuff(a="test", b=2)


def test_invalid() -> None:
    with pytest.raises(Exception):
        Stuff(a="test", b=-1)
