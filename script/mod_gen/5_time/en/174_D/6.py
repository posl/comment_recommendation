def solve(N, C):
    W = 0
    for i in range(N):
        if C[i] == "W":
            W += 1
    if W == 0 or W == N:
        return 0
    l = 0
    r = N - 1
    ans = 0
    while l < r:
        if C[l] == "W" and C[r] == "R":
            ans += 1
            l += 1
            r -= 1
        elif C[l] == "W":
            r -= 1
        elif C[r] == "R":
            l += 1
        else:
            l += 1
            r -= 1
    return ans
N = int(input())
C = input()
print(solve(N, C))
