def solve():
    N, K = map(int, input().split())
    AB = []
    for _ in range(N):
        A, B = map(int, input().split())
        AB.append((A, B))
    AB.sort()
    ans = K
    for i in range(N):
        A, B = AB[i]
        if ans < A:
            break
        ans += B
    print(ans)
