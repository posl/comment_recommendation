def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    ans = float('inf')
    for i in range(N-K+1):
        left = x[i]
        right = x[i+K-1]
        ans = min(ans, abs(left) + abs(left - right), abs(right) + abs(left - right))
    print(ans)
