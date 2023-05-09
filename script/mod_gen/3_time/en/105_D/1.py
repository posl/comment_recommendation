def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for i in range(N):
        B[i + 1] = (B[i] + A[i]) % M
    from collections import defaultdict
    d = defaultdict(int)
    for b in B:
        d[b] += 1
    ans = 0
    for v in d.values():
        ans += v * (v - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()