def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N, K) + 1):
            if i + j > K:
                continue
            if i + j > N:
                continue
            tmp = sum(V[:i]) + sum(V[-j:])
            tmp = sorted(tmp)
            tmp = tmp[min(i + j, K)]
            ans = max(ans, tmp)
    print(ans)
