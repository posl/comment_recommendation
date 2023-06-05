def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    visited = [False] * N
    visited[0] = True
    i = 0
    for k in range(K):
        i = A[i] - 1
        if visited[i]:
            break
        visited[i] = True
    if k == K - 1:
        print(i + 1)
    else:
        K -= k
        K %= k
        for i in range(N):
            if visited[i]:
                K -= 1
                if K == 0:
                    print(i + 1)
                    break
