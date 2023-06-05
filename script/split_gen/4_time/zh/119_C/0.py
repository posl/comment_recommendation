def solve(N, A, B, C, L):
    ans = 10**9
    for i in range(4**N):
        a = i
        mp = 0
        p = [0, 0, 0]
        for j in range(N):
            if a % 4 == 1:
                mp += 10
                p[0] += L[j]
            elif a % 4 == 2:
                mp += 10
                p[1] += L[j]
            elif a % 4 == 3:
                mp += 10
                p[2] += L[j]
            a //= 4
        if p[0] == 0 or p[1] == 0 or p[2] == 0:
            continue
        mp += abs(A - p[0]) + abs(B - p[1]) + abs(C - p[2])
        ans = min(ans, mp)
    return ans
N, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(N)]
print(solve(N, A, B, C, L))
