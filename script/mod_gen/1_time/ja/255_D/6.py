def main():
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    X = [int(input()) for _ in range(Q)]
    D = [0 for _ in range(N+1)]
    for i in range(N):
        D[i+1] = A[i] - A[i-1]
    for x in X:
        ans = 0
        for i in range(N):
            if D[i] > 0:
                ans += min(D[i],x)
            else:
                ans += max(D[i],-x)
        print(ans)

if __name__ == '__main__':
    main()