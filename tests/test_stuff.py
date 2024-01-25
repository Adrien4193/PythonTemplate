import pytest

from template import Stuff


def test_ok() -> None:
    Stuff("test", 2)


def test_invalid() -> None:
    with pytest.raises(Exception):
        Stuff("test", -1)
