def main():
    N, X, Y = map(int, input().strip().split())
    ans = [0 for i in range(N)]
    for i in range(1, N):
        for j in range(i+1, N+1):
            k = min(j-i, abs(X-i)+1+abs(Y-j), abs(Y-i)+1+abs(X-j))
            ans[k] += 1
    for i in range(1, N):
        print(ans[i])

if __name__ == '__main__':
    main()