def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N, K) + 1 - i):
            temp = V[:i] + V[N - j:]
            temp.sort()
            ans = max(ans, sum(temp[K - i - j:]))
    print(ans)
