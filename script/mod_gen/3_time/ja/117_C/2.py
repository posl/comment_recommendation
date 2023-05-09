def main():
    N,M = map(int,input().split())
    X = list(map(int,input().split()))
    X.sort()
    L = []
    for i in range(M-1):
        L.append(X[i+1]-X[i])
    L.sort()
    ans = 0
    for i in range(M-N):
        ans += L[i]
    print(ans)

if __name__ == '__main__':
    main()