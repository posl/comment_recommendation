def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = (S[i] + A[i]) % M
    from collections import Counter
    cnt = Counter(S)
    ans = 0
    for v in cnt.values():
        ans += v * (v - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()