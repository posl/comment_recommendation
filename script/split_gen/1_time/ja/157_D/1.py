def main():
    N, M, K = map(int, input().split())
    friend = [set() for _ in range(N)]
    block = [set() for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        A -= 1
        B -= 1
        friend[A].add(B)
        friend[B].add(A)
    for _ in range(K):
        C, D = map(int, input().split())
        C -= 1
        D -= 1
        block[C].add(D)
        block[D].add(C)
    ans = [0] * N
    for i in range(N):
        ans[i] = len(friend[i] - block[i] - set([i])) - 1
    print(*ans)
