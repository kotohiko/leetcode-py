class Solution:
    """
    Url:
        https://leetcode.cn/problems/add-binary/description/
    Author:
        Jacob Suen
    Time:
        08:03 Jul 10th, 2024
    """

    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]


def stringToString(input):
    import json

    return json.loads(input)


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
            a = stringToString(line)
            line = next(lines)
            b = stringToString(line)

            ret = Solution().addBinary(a, b)

            out = ret
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
