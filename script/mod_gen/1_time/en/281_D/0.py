def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    S = set()
    for i in range(1 << N):
        if bin(i).count("1") == K:
            S.add(sum(A[j] for j in range(N) if (i >> j) & 1))
    ans = -1
    for i in sorted(S, reverse=True):
        if i % D == 0:
            ans = i
            break
    print(ans)

if __name__ == '__main__':
    main()