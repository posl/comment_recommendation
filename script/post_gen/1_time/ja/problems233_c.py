Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    ans = 0
    for i in range(2**N):
        num = 1
        for j in range(N):
            if ((i >> j) & 1):
                num *= L[j][1]
            else:
                num *= L[j][2]
        if num <= X:
            ans += 1
    print(ans)

=======
Suggestion 2

def get_divisor(n):
    divisor = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisor.append(i)
            if i != n // i:
                divisor.append(n//i)
    return divisor

=======
Suggestion 3

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

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    #print(N, X)
    #print(A)
    ans = 0
    for i in range(1, 2**N):
        #print("i:", i)
        tmp = 1
        for j in range(N):
            if i & 1 << j:
                #print("j:", j)
                tmp *= A[j][0]
        #print("tmp:", tmp)
        if tmp > X:
            continue
        #print("i:", i)
        for j in range(N):
            if i & 1 << j:
                #print("j:", j)
                for k in range(1, A[j][0]+1):
                    #print("k:", k)
                    if tmp * A[j][k] == X:
                        ans += 1
                    elif tmp * A[j][k] > X:
                        break
    print(ans)

=======
Suggestion 5

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    #print(N, X)
    #print(L)
    ans = 0
    for i in range(2**N):
        a = [0 for j in range(N)]
        for j in range(N):
            if (i >> j) & 1:
                a[j] = 1
        #print(a)
        tmp = 1
        for j in range(N):
            if a[j] == 1:
                tmp *= L[j][a[j]]
        if tmp == X:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    import sys
    input = sys.stdin.readline

    N, X = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    #print(N, X)
    #print(A)

    #A = [[3, 1, 8, 4], [2, 10, 5]]
    #X = 40

    #A = [[3, 10, 10, 10], [3, 10, 10, 10], [5, 2, 2, 2, 2, 2]]
    #X = 200

    #A = [[2, 1000000000, 1000000000], [2, 1000000000, 1000000000], [2, 1000000000, 1000000000]]
    #X = 1000000000000000000

    #A = [[2, 1, 1], [2, 2, 2], [2, 3, 3]]
    #X = 36

    #A = [[3, 1, 2, 3], [3, 2, 3, 4], [3, 3, 4, 5]]
    #X = 120

    #A = [[3, 1, 2, 3], [3, 2, 3, 4], [3, 3, 4, 5]]
    #X = 120

    #A = [[2, 1, 1], [2, 1, 1], [2, 1, 1]]
    #X = 1

    #A = [[2, 1, 1], [2, 1, 1], [2, 1, 1]]
    #X = 2

    #A = [[2, 1, 1], [2, 1, 1], [2, 1, 1]]
    #X = 3

    #A = [[2, 1, 1], [2, 1, 1], [2, 1, 1]]
    #X = 4

    #A = [[2, 1, 1], [

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    A = []
    for i in range(N):
        L = list(map(int, input().split()))
        A.append(L[1:])
    #print(A)

    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(len(A[i])):
                for l in range(len(A[j])):
                    if A[i][k] * A[j][l] == X:
                        cnt += 1
    print(cnt)

=======
Suggestion 9

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

=======
Suggestion 10

def main():
    N, X = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    #print(A) #A[0][1] A[1][1] A[2][1] がそれぞれ最初の袋の2番目のボールの書かれた数
    #print(A[0][1]) #A[0][1] が最初の袋の2番目のボールの書かれた数
    #print(A[1][1]) #A[1][1] が2番目の袋の2番目のボールの書かれた数
    #print(A[2][1]) #A[2][1] が3番目の袋の2番目のボールの書かれた数
    #print(A[0][2]) #A[0][2] が最初の袋の3番目のボールの書かれた数
    #print(A[1][2]) #A[1][2] が2番目の袋の3番目のボールの書かれた数
    #print(A[2][2]) #A[2][2] が3番目の袋の3番目のボールの書かれた数
    #print(A[0][3]) #A[0][3] が最初の袋の4番目のボールの書かれた数
    #print(A[1][3]) #A[1][3] が2番目の袋の4番目のボールの書かれた数
    #print(A[2][3]) #A[2][3] が3番目の袋の4番目のボールの書かれた数
    #print(A[0][4]) #A[0][4] が最初の袋の5番目のボールの書かれた数
    #print(A[1][4]) #A[1][4] が2番目
