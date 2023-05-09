def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    ans = float('inf')
    for i in range(N-K+1):
        left = x[i]
        right = x[i+K-1]
        if left >= 0:
            ans = min(ans, right - left)
        elif right <= 0:
            ans = min(ans, abs(left) + abs(right))
        else:
            ans = min(ans, abs(left) + right + min(abs(left), right))
    print(ans)

if __name__ == '__main__':
    main()