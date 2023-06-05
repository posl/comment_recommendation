def main():
    N, K = map(int, input().split())
    X = list(map(int, input().split()))
    ans = float('inf')
    for i in range(N-K+1):
        left = X[i]
        right = X[i+K-1]
        if left * right <= 0:
            ans = min(ans, min(abs(left), abs(right)) * 2 + max(abs(left), abs(right)))
        else:
            ans = min(ans, max(abs(left), abs(right)))
    print(ans)
