def main():
    N, M, K = map(int, input().split())
    block = [[] for _ in range(N)]
    friend = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        friend[a-1].append(b-1)
        friend[b-1].append(a-1)
    for _ in range(K):
        c, d = map(int, input().split())
        block[c-1].append(d-1)
        block[d-1].append(c-1)
    ans = [0] * N
    for i in range(N):
        ans[i] = N - len(friend[i]) - 1
        for j in block[i]:
            if j in friend[i]:
                ans[i] -= 1
    for i in range(N):
        for j in friend[i]:
            if i < j:
                ans[i] -= 1
                ans[j] -= 1
    print(*ans)
