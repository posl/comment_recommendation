def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for l in range(min(N, K) + 1):
        for r in range(min(N, K) - l + 1):
            if l + r > N or l + r > K:
                continue
            if l + r == 0:
                continue
            tmp = []
            for i in range(l):
                tmp.append(V[i])
            for i in range(r):
                tmp.append(V[N - 1 - i])
            tmp.sort()
            cnt = K - l - r
            for i in range(min(cnt, len(tmp))):
                if tmp[i] < 0:
                    tmp[i] = 0
            ans = max(ans, sum(tmp))
    print(ans)

if __name__ == '__main__':
    main()