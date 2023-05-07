def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    S = set()
    for i in range(1 << N):
        if bin(i).count('1') == K:
            s = 0
            for j in range(N):
                if (i >> j) & 1:
                    s += A[j]
            S.add(s)
    S = sorted(list(S))
    if S[-1] < D:
        print(-1)
    else:
        for i in range(len(S)-1, -1, -1):
            if S[i] % D == 0:
                print(S[i])
                break

if __name__ == '__main__':
    main()