def main():
    N, X = map(int, input().split())
    A = [[] for _ in range(N)]
    for i in range(N):
        L = list(map(int, input().split()))
        A[i] = L[1:]
    ans = 0
    for i in range(1, 2**N):
        tmp = 1
        for j in range(N):
            if (i >> j) & 1:
                tmp *= A[j][0]
            else:
                tmp *= A[j][1]
        if tmp == X:
            ans += 1
    print(ans)
