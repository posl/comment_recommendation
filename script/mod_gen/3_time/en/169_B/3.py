def solve():
    N = int(input())
    A = list(map(int, input().split()))
    if 0 in A:
        return 0
    ans = 1
    for a in A:
        ans *= a
        if ans > 10 ** 18:
            return -1
    return ans
print(solve())
