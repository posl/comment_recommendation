def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(N, K) + 1):
        for j in range(min(N, K) - i + 1):
            if i + j > K:
                continue
            tmp = sorted(V[:i] + V[N - j:])
            tmp_sum = sum(tmp)
            for k in range(min(i + j, len(tmp))):
                if tmp[k] >= 0:
                    break
                tmp_sum -= tmp[k]
            ans = max(ans, tmp_sum)
    print(ans)

if __name__ == '__main__':
    main()