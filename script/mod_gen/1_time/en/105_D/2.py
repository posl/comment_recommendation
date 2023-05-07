def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    for i in range(1, N+1):
        A[i] = (A[i-1] + A[i]) % M
    from collections import defaultdict
    d = defaultdict(int)
    for a in A:
        d[a] += 1
    ans = 0
    for k in d:
        ans += d[k] * (d[k] - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()