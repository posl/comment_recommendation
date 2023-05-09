def main():
    N, K = map(int, input().split())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    A.sort()
    A = [list(x) for x in zip(*A)]
    A.sort()
    A = [list(x) for x in zip(*A)]
    ans = 10 ** 9
    for i in range(N - K + 1):
        for j in range(N - K + 1):
            tmp = []
            for k in range(K):
                tmp.extend(A[i + k][j:j + K])
            tmp.sort()
            ans = min(ans, tmp[K ** 2 // 2])
    print(ans)
