def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    acc = 0
    accs = [0]
    for i in range(N):
        acc += A[i]
        accs.append(acc)
    ans = 0
    for i in range(N+1):
        for j in range(i+1, N+1):
            if accs[j] - accs[i] >= K:
                ans += 1
    print(ans)
