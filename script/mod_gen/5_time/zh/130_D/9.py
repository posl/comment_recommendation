def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    cumsum = [0]
    for i in range(N):
        cumsum.append(cumsum[i] + A[i])
    ans = 0
    # しゃくとり法
    r = 0
    for l in range(N):
        while r < N + 1 and cumsum[r] - cumsum[l] < K:
            r += 1
        ans += N - r + 1
    print(ans)

if __name__ == '__main__':
    main()