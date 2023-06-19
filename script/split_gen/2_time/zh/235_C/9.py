def solve():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    for _ in range(Q):
        x, k = map(int, input().split())
        cnt = 0
        for i in range(N):
            if A[i] == x:
                cnt += 1
                if cnt == k:
                    print(i + 1)
                    break
        else:
            print(-1)
solve()
