def main():
    N, K = map(int, input().split())
    S = [input() for i in range(N)]
    ans = 0
    for i in range(1 << N):
        if bin(i).count('1') != K:
            continue
        A = []
        for j in range(N):
            if (i >> j) & 1:
                A.append(S[j])
        C = set(''.join(A))
        if len(C) == K:
            ans = max(ans, len(C))
    print(ans)

if __name__ == '__main__':
    main()