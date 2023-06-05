def solve(S):
    if S < 3:
        return 0
    else:
        ans = 1
        for i in range(1, S):
            ans *= 2
            ans %= 1000000007
        return ans
S = int(input())
print(solve(S))
