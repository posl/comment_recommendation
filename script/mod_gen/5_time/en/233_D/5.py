def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    for i in range(N):
        A[i+1] += A[i]
    from collections import defaultdict
    d = defaultdict(int)
    ans = 0
    for i in range(N+1):
        ans += d[A[i]-K]
        d[A[i]] += 1
    print(ans)

if __name__ == '__main__':
    main()