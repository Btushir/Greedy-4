"""
source = "abc", target = "abcbc"
Brute force: form all the subsequences then combine those and see if any of them matches with target.
TC: O(2^n)
2 pointers: TC: O(m*n)

binary search: TC: O(n * log (k)), k is average list size, since this is list on which we do binary search,
 SC: O(m)
"""


class Solution_two_ointer:
    def shortestWay(self, source: str, target: str) -> int:

        i = 0
        j = 0  # i: target, j: source
        count = 0
        # need to maintian a visited set to check if the target ch is there or not
        visited = set()

        for ch in source:
            visited.add(ch)

        while i < len(target):  # acdbc

            if target[i] not in visited:
                count = -1
                return count
            while j < len(source):  # abc
                # since i is incremented in the inner while loop
                # it is possible target will be reached
                if i == len(target):
                    return count + 1
                if source[j] == target[i]:  #
                    i += 1
                    j += 1
                elif source[j] != target[i]:
                    j += 1

            if j == len(source):
                # index i is not incremented
                count += 1
                j = 0

        return count


class Solution_binary_search:
    def binary_search(self, lst, target):
        lo, hi = 0, len(lst) - 1
        while (lo <= hi):
            mid = lo + (hi - lo) // 2
            if lst[mid] == target:
                return mid

            elif lst[mid] > target:
                hi = mid - 1

            else:
                lo = mid + 1

        return lo

    def shortestWay(self, source: str, target: str) -> int:

        hmap = {}

        for idx, ch in enumerate(source):
            if ch not in hmap:
                hmap[ch] = []
            hmap[ch].append(idx)

        count = 0
        i = 0
        j = 0
        while i < len(target):  # acdbc
            if target[i] not in hmap:
                return -1

            lst = hmap[target[i]]
            lst_idx = self.binary_search(lst, j)
            # this is when no valid index in the source is found
            # this means there is no valid occurrence of the character
            # in source at or after the current position. It is present previously.
            if lst_idx >= len(lst):
                j = 0
                count += 1
            else:
                i += 1
                j = lst[lst_idx] + 1

            if i == len(target):
                return count + 1

        return count
