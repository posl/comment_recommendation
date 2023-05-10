def main():
    N,X,Y = map(int,input().split())
    N = N + 1
    X = X - 1
    Y = Y - 1
    ans = [0 for i in range(N)]
    for i in range(N-1):
        for j in range(i+1,N):
            dist = min(j-i,abs(X-i)+1+abs(Y-j),abs(Y-i)+1+abs(X-j))
            ans[dist] = ans[dist] + 1
    for i in range(1,N):
        print(ans[i])

if __name__ == '__main__':
    main()