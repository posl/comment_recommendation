def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(K + 1):
        for j in range(K - i + 1):
            if i + j > N:
                continue
            tmp = V[:i] + V[N-j:]
            tmp.sort()
            ans = max(ans, sum(tmp[max(0, i + j - K):]))
    print(ans)
