def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    ans = 10 ** 9
    for i in range(N - K + 1):
        left = x[i]
        right = x[i + K - 1]
        ans = min(ans, right - left + min(abs(left), abs(right)))
    print(ans)
