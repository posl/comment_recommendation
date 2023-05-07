def main():
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    ans = 0
    for a in range(min(N, K) + 1):
        for b in range(min(N, K) - a + 1):
            T = V[:a] + V[N - b:]
            T.sort()
            s = sum(T)
            for i in range(min(K - a - b, len(T))):
                if T[i] < 0:
                    s -= T[i]
                else:
                    break
            ans = max(ans, s)
    print(ans)

if __name__ == '__main__':
    main()