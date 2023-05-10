def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    ans = 10**9
    for i in range(N-K+1):
        left = X[i]
        right = X[i+K-1]
        if left < 0 and right < 0:
            ans = min(ans, abs(left))
        elif left < 0 and right >= 0:
            ans = min(ans, abs(left)*2 + abs(right))
        else:
            ans = min(ans, abs(right))
    print(ans)

if __name__ == '__main__':
    main()