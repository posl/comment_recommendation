def solve():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if P[i] == i:
            ans += 1
            if i < N-1 and P[i+1] == i+1:
                P[i], P[i+1] = P[i+1], P[i]
            elif i == N-1 and P[0] == 0:
                P[i], P[0] = P[0], P[i]
    print(ans)
