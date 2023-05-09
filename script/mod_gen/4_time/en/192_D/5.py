def solve(x, m):
    d = int(max(x))
    if len(x) == 1:
        if int(x) <= m:
            return 1
        else:
            return 0
    elif d == 1:
        return len(x)
    else:
        l = 0
        r = m + 1
        while r - l > 1:
            mid = (r + l) // 2
            if int(x, mid) <= m:
                l = mid
            else:
                r = mid
        return l - d
x = input()
m = int(input())
print(solve(x, m))
from sys import stdin
from math import log

if __name__ == '__main__':
    solve()