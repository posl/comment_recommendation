def solve(L):
    if L < 12:
        return 0
    elif L == 12:
        return 1
    elif L > 12:
        return solve(L-1) + solve(L-4) + solve(L-7) + solve(L-10) + solve(L-12)
L = int(input())
print(solve(L))
