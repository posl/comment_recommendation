def main():
    from bisect import bisect_left, bisect_right
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    #print(X)
    ans = 0
    for i in range(M-1):
        ans += X[i+1] - X[i]
    #print(ans)
    for i in range(M-1):
        ans -= max(0, X[i+1] - X[i] - 1)
    #print(ans)
    print(ans)

if __name__ == '__main__':
    main()