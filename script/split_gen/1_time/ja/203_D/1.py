def main():
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 10**9
    for i in range(N-K+1):
        for j in range(N-K+1):
            a = []
            for x in range(K):
                for y in range(K):
                    a.append(A[i+x][j+y])
            a.sort()
            ans = min(a[K*K//2], ans)
    print(ans)
