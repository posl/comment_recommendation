def solve():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        if sum([a*b for a, b in zip(A[i], B)]) + C > 0:
            ans += 1
    print(ans)
