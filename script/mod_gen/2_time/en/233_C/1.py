def main():
    N, X = map(int, input().split())
    L = [0] * N
    A = [[] for _ in range(N)]
    for i in range(N):
        L[i], *A[i] = map(int, input().split())
    #print(L, A)
    ans = 0
    for i in range(2**N):
        p = 1
        for j in range(N):
            if (i >> j) & 1:
                p *= A[j][0]
            else:
                p *= A[j][-1]
        if p <= X:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()