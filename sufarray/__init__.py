"Sufarray: Python-only implementation of suffix array"

import bisect
import functools
import typing


# Needed until we replace our algorithm, otherwise sort() tries to
# keep all our suffixes to speed up the sorting, but that makes the
# module very memory hungry
@functools.total_ordering
class _SortKey:
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
    
    def __lt__(self, other):
        return self.text[self.pos:] < other.text[other.pos:]


class SufArray:
    """Represent a suffix array

    At present the implementation is not fast, but it will be
    optimized later.

    Args:
        text: The underlying text

    """
    def __init__(self, text: str) -> None:
        self._text = text
        self._array = self._compute_sufarray()

    def _compute_sufarray(self):
        def _key(pos):
            return _SortKey(self._text, pos)
        return sorted(range(len(self._text)), key=_key)

    def get_array(self) -> typing.List[int]:
        """Get the built suffix array

        If len(text) = n, then the returned array ret is a permutation
        of list(range(n)), where the suffix of text starting at
        position ret[i] is guaranteed to be less than that of ret[i+1]
        in lexicographic order, for all i from 0 to n-1.

        """
        return self._array

    def find_all(self, substr: str) -> typing.Iterable[int]:
        """Find the all occurrences of a string

        Args:
            substr: The string to search

        Returns:
            Generator of positions

        """
        left = self._bisect_left(substr)
        right = self._bisect_right(substr)
        while left < right:
            yield self._array[left]
            left += 1

    def _bisect_left(self, substr: str) -> int:
        # Return smallest i such that substr is smaller than or equal
        # to self._text[self._array[i] : self._array[i] +
        # len(substr)].  If there is no such i, return len(self._text)
        left = 0
        right = len(self._text)
        while left < right:
            mid = (left + right) // 2  # right will never be checked
            pos = self._array[mid]
            if substr <= self._text[pos : pos + len(substr)]:
                right = mid
            else:
                left = mid + 1
        return left

    def _bisect_right(self, substr: str) -> int:
        # Return largest i such that substr is larger than or equal to
        # self._text[self._array[i-1] : self._array[i-1] + len(substr)].
        # If there is no such i, return 0
        left = 0
        right = len(self._text)
        while left < right:
            mid = (left + right + 1) // 2  # left will never be checked
            pos = self._array[mid - 1]
            if substr >= self._text[pos : pos + len(substr)]:
                left = mid
            else:
                right = mid - 1
        return left
