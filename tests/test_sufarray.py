import typing

import sufarray


def find_all(sarray: sufarray.SufArray, needle: str) -> typing.List[int]:
    return list(sarray.find_all(needle))


def test_empty():
    sarray = sufarray.SufArray('')
    assert sarray.get_array() == []
    assert find_all(sarray, 'a') == []


def test_single():
    sarray = sufarray.SufArray('a')
    assert sarray.get_array() == [0]
    assert find_all(sarray, 'a') == [0]
    assert find_all(sarray, '0') == []
    assert find_all(sarray, 'b') == []


def test_basic():
    sarray = sufarray.SufArray('banana')
    assert sarray.get_array() == [5, 3, 1, 0, 4, 2]
    assert find_all(sarray, 'a') == [5, 3, 1]
    assert find_all(sarray, 'na') == [4, 2]
    assert find_all(sarray, '0') == []
    assert find_all(sarray, 'z') == []


def test_long():
    sarray = sufarray.SufArray('a' * 300000)
    assert sarray.get_array() == list(reversed(range(300000)))
