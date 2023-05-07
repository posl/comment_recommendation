def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(K + 1):
        for j in range(K + 1 - i):
            if i + j > N:
                continue
            tmp = V[:i] + V[N - j:]
            tmp.sort()
            for k in range(K - i - j):
                if k < len(tmp) and tmp[k] < 0:
                    tmp[k] = 0
                else:
                    break
            ans = max(ans, sum(tmp))
    print(ans)
