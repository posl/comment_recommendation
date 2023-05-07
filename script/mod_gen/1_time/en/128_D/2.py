def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for i in range(min(K, N) + 1):
        for j in range(min(K - i, N) + 1):
            if i + j == 0:
                continue
            tmp = V[:i] + V[N-j:]
            tmp.sort()
            for k in range(min(K - i - j, i + j)):
                if tmp[k] >= 0:
                    break
                tmp[k] = 0
            ans = max(ans, sum(tmp))
    print(ans)

if __name__ == '__main__':
    main()