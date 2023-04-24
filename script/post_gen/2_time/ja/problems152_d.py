Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = [0] * 10
    B = [0] * 10
    for i in range(1, N+1):
        A[i//10] += 1
        B[i%10] += 1
    ans = 0
    for i in range(10):
        for j in range(10):
            if i == j:
                ans += A[i] * B[j]
            else:
                ans += A[i] * B[j]
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if i < 10:
            ans += 1
        elif i < 100:
            ans += 9
        elif i < 1000:
            ans += 90
        elif i < 10000:
            ans += 900
        elif i < 100000:
            ans += 9000
        else:
            ans += 90000
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    ans = 0
    for i in range(1,n+1):
        if i % 10 == 0:
            continue
        for j in range(1,n+1):
            if j % 10 == 0:
                continue
            if str(i)[-1] == str(j)[0]:
                ans += 1
    print(ans)

main()

=======
Suggestion 4

def main():
    N = int(input())
    #N以下の正の整数の組(A,B)の個数を求める
    #A,Bを先頭に0のつかない10進数表記で表したときに、
    #Aの末尾の桁がBの先頭の桁に等しく、Aの先頭の桁がBの末尾の桁に等しい
    #A,Bの桁数は同じ
    #Nは10^5以下
    #A,BはN以下
    #N=1のときは1
    #N=2のときは1
    #N=3のときは2
    #N=4のときは3
    #N=5のときは4
    #N=6のときは5
    #N=7のときは6
    #N=8のときは7
    #N=9のときは8
    #N=10のときは9
    #N=11のときは9
    #N=12のときは10
    #N=13のときは11
    #N=14のときは12
    #N=15のときは13
    #N=16のときは14
    #N=17のときは15
    #N=18のときは16
    #N=19のときは17
    #N=20のときは18
    #N=21のときは18
    #N=22のときは19
    #N=23のときは20
    #N=24のときは21
    #N=25のときは22
    #N=26のときは23
    #N=27のときは24
    #N=28のときは25
    #N=29のときは26
    #N=30のときは27
    #N=31のときは27
    #N=32のときは28
    #N=33のときは29

=======
Suggestion 5

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i%10 == j//10**int(len(str(j)))-1:
                ans += 1
    print(ans)
    return

=======
Suggestion 6

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if i < 10:
            ans += 1
        else:
            if i % 10 == (i // 10) % 10:
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    ans = 0
    # 0~9の数のリストを作成
    num = [0,0,0,0,0,0,0,0,0,0]
    for i in range(1,N+1):
        # 一桁目と一番下の桁の数字を取得
        first = int(str(i)[0])
        last = int(str(i)[-1])
        # 一桁目の数字のリストの要素に1を足す
        num[first] += 1
        # 一番下の桁の数字のリストの要素に1を足す
        num[last] += 1
    # 0~9の数のリストの要素を2で割る
    for i in range(10):
        num[i] = num[i] // 2
    # 0~9の数のリストの要素を足す
    for i in range(10):
        ans += num[i]
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    print(N * (N + 1) // 2)

=======
Suggestion 9

def count (n):
    if n < 10:
        return 1
    else:
        return 10 * count(n // 10) + 8 * 9 * (n // 10 - 1)

=======
Suggestion 10

def main():
    N = int(input())
    #1の位の数をkeyにして、個数をvalueにする辞書を作る
    #例：1の位が0の数は0個
    #例：1の位が1の数は1個
    #例：1の位が2の数は2個
    #例：1の位が3の数は3個
    #例：1の位が4の数は4個
    #例：1の位が5の数は5個
    #例：1の位が6の数は6個
    #例：1の位が7の数は7個
    #例：1の位が8の数は8個
    #例：1の位が9の数は9個
    #例：1の位が0の数は0個
    #例：1の位が1の数は1個
    #例：1の位が2の数は2個
    #例：1の位が3の数は3個
    #例：1の位が4の数は4個
    #例：1の位が5の数は5個
    #例：1の位が6の数は6個
    #例：1の位が7の数は7個
    #例：1の位が8の数は8個
    #例：1の位が9の数は9個
    #例：1の位が0の数は0個
    #例：1の位が1の数は1個
    #例：1の位が2の数は2個
    #例：1の位が3の数は3個
    #例：1の位が4の数は4個
    #例：1の位が5の数は5個
    #例：1の位が6の数は6個
    #例：1の位が7の数は7個
    #例：1の位が8の数は8個
