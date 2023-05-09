def main():
    N, X, Y = map(int, input().split())
    ans = [0] * (N-1)
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            dist = min(j-i, abs(X-i) + 1 + abs(j-Y))
            ans[dist-1] += 1
    for i in range(N-1):
        print(ans[i])

if __name__ == '__main__':
    main()