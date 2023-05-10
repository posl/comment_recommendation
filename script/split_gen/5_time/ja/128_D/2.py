def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for l in range(min(K, N) + 1):
        for r in range(min(K, N) + 1):
            if l + r > min(K, N):
                continue
            if l + r > N:
                continue
            if l + r > K:
                continue
            # print(l, r)
            tmp = []
            for i in range(l):
                tmp.append(V[i])
            for i in range(r):
                tmp.append(V[N - 1 - i])
            tmp.sort()
            # print(tmp)
            for i in range(min(K - l - r, len(tmp))):
                if tmp[i] < 0:
                    tmp[i] = 0
            # print(tmp)
            ans = max(ans, sum(tmp))
    print(ans)
