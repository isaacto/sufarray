import typing

import sufarray


def find_all(sarray: sufarray.SufArray, needle: str) -> typing.List[int]:
    return list(sarray.find_all(needle))


def test_empty():
    for impl in [sufarray.SufArrayBruteForce, sufarray.SufArrayPD]:
        sarray = impl('')
        assert sarray.get_array() == []
        assert find_all(sarray, 'a') == []


def test_single():
    for impl in [sufarray.SufArrayBruteForce, sufarray.SufArrayPD]:
        sarray = impl('a')
        assert sarray.get_array() == [0]
        assert find_all(sarray, 'a') == [0]
        assert find_all(sarray, '0') == []
        assert find_all(sarray, 'b') == []


def test_basic():
    for impl in [sufarray.SufArrayBruteForce, sufarray.SufArrayPD]:
        sarray = impl('banana')
        assert sarray.get_array() == [5, 3, 1, 0, 4, 2]
        assert find_all(sarray, 'a') == [5, 3, 1]
        assert find_all(sarray, 'na') == [4, 2]
        assert find_all(sarray, '0') == []
        assert find_all(sarray, 'z') == []
        for cnt in range(100):
            sarray = impl('aabaaabaaacaaadaac' + '0' * cnt)
            assert find_all(sarray, 'aac') == [15, 8]


def test_long():
    for impl in [sufarray.SufArrayBruteForce, sufarray.SufArrayPD]:
        tlen = 3000
        sarray = impl('a' * tlen)
        assert sarray.get_array() == list(reversed(range(tlen)))
        assert next(sarray.find_all('')) == tlen - 1
        for n in range(1, tlen // 2):
            assert next(sarray.find_all('a' * n)) == tlen - n
