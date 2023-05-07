def main():
    import sys
    from itertools import combinations
    from math import gcd
    N, X = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    print(A)
    # 総積が X になる取り出し方が 1 つも存在しないこともあります。
    # なので、最初に X が A の中に存在するかチェックする。
    for i in range(N):
        if X in A[i]:
            print(1)
            sys.exit()
    # A の中に X が存在しない場合、総積が X になる取り出し方は、
    # A の中の数字の組み合わせで作れるかどうかをチェックする。
    # そのために、A の中の数字の組み合わせを全て作る。
    # その組み合わせの中で、X と互いに素なものをカウントする。
    count = 0
    for i in range(2, N+1):
        for j in combinations(range(N), i):
            #print(j)
            #print(A[j[0]][1])
            #print(A[j[1]][1])
            #print(A[j[2]][1])
            #print(A[j[3]][1])
            #print(A[j[4]][1])
            # A の中の数字の組み合わせを全て作る。
            # その組み合わせの中で、X と互いに素なものをカウントする。
            # そのために、組み合わせの中の数字を全て掛け合わせる。
            # その結果が X と互いに素なら、カウントする。
            # なお、X と互いに素なら、gcd は 1 になる。
            #print(gcd(X, A[j[0]][1]))
            #print(gcd(X, A[j[1]][1]))
            #print(g

if __name__ == '__main__':
    main()