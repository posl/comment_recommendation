def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N, K) - i + 1):
            arr = V[:i] + V[N - j:]
            arr.sort()
            tmp = 0
            for k in range(min(K - i - j, len(arr))):
                if arr[k] < 0:
                    arr[k] = 0
            tmp = sum(arr)
            ans = max(ans, tmp)
    print(ans)
