def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a % M for a in A]
    A = [0] + A
    for i in range(1, N + 1):
        A[i] = (A[i] + A[i - 1]) % M
    d = {}
    for a in A:
        if a in d:
            d[a] += 1
        else:
            d[a] = 1
    ans = 0
    for a in d:
        ans += d[a] * (d[a] - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()