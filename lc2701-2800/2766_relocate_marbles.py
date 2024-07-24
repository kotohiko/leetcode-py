import json
from typing import List


class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        st = set(nums)
        for f, t in zip(moveFrom, moveTo):
            st.remove(f)
            st.add(t)
        return sorted(st)


def stringToIntegerList(input):
    return json.loads(input)


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line);
            line = next(lines)
            moveFrom = stringToIntegerList(line);
            line = next(lines)
            moveTo = stringToIntegerList(line);

            ret = Solution().relocateMarbles(nums, moveFrom, moveTo)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
