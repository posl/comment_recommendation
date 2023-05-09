def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    S = set()
    for i in range(1 << N):
        if bin(i).count("1") == K:
            S.add(sum(A[j] for j in range(N) if (i >> j) & 1))
    for num in range((max(S) // D) * D, -1, -D):
        if num in S:
            print(num)
            return
    print(-1)

if __name__ == '__main__':
    main()