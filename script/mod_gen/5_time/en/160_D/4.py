def main():
    N, X, Y = map(int, input().split())
    #print(N, X, Y)
    ans = [0 for i in range(N-1)]
    for i in range(1, N):
        for j in range(i+1, N+1):
            d = min(abs(i-j), abs(X-i)+1+abs(Y-j), abs(Y-i)+1+abs(X-j))
            ans[d-1] += 1
    for i in range(N-1):
        print(ans[i])

if __name__ == '__main__':
    main()