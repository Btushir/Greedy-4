"""
Brute force: traverse 1 to 6, and check if 1 is probable then check if valid.
TC: 6 * O(n)
probable candidate: the frequency of that number should be >= len(lst). This is because in the end, the number
should appear on all the tiles. To do so, there should be that many occurrences of that number.
However, having the freq does not mean we can get a valid answer. Thus, need to scan the array and check for validate.
TC: O(n) to find the probable number + O(n) to check if the probable number is valid.
SC: O(n)
it is possible there are 2 probable candidates. Note that the answer would be same both.
example: tops: 3,2,2 and bottoms: 2,3,3. Minimum number of rotations would be same for both 3 and 2.


"""


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:

        hmap = {}
        proba_num = None
        for num in tops:
            if num not in hmap:
                hmap[num] = 0
            hmap[num] += 1

        for num in bottoms:
            if num not in hmap:
                hmap[num] = 0
            hmap[num] += 1
            if hmap[num] >= len(tops):
                proba_num = num
                break

        print(hmap, proba_num)
        if not proba_num:
            return -1

        top_min = 0
        bot_min = 0
        for idx in range(len(tops)):
            if tops[idx] != proba_num and bottoms[idx] != proba_num:
                return -1

            elif tops[idx] == proba_num and bottoms[idx] != proba_num:
                bot_min += 1

            elif tops[idx] != proba_num and bottoms[idx] == proba_num:
                top_min += 1

        return min(top_min, bot_min)

