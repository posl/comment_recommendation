def main():
    #入力
    N, X = map(int, input().split())
    L = [0] * N
    A = [0] * N
    for i in range(N):
        L[i] = list(map(int, input().split()))
        A[i] = L[i][1:]
    #組み合わせを列挙
    import itertools
    comb = list(itertools.product(*A))
    #組み合わせに対して総積を計算
    #総積がXになるものをカウント
    ans = 0
    for i in range(len(comb)):
        tmp = 1
        for j in range(N):
            tmp *= comb[i][j]
        if tmp == X:
            ans += 1
    #出力
    print(ans)

if __name__ == '__main__':
    main()