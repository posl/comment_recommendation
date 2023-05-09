def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for a in range(min(N, K) + 1):
        for b in range(min(N - a, K - a) + 1):
            tmp = V[:a] + V[N - b:]
            tmp.sort()
            for i in range(K - a - b):
                if len(tmp) == 0:
                    break
                if tmp[0] > 0:
                    break
                tmp.pop(0)
            ans = max(ans, sum(tmp))
    print(ans)
