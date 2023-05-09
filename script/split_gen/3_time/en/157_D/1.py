def main():
    N, M, K = map(int, input().split())
    friend = [set() for _ in range(N)]
    block = [set() for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        friend[a-1].add(b-1)
        friend[b-1].add(a-1)
    for _ in range(K):
        c, d = map(int, input().split())
        block[c-1].add(d-1)
        block[d-1].add(c-1)
    for i in range(N):
        ans = N - len(friend[i]) - 1
        for j in friend[i]:
            ans -= len(friend[j] & block[i])
        print(ans, end=' ')
