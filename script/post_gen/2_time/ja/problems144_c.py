Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    cnt = 0
    i = 1
    while i < N:
        i += i
        cnt += 1
    print(cnt)

=======
Suggestion 2

def main():
    n = int(input())
    x = 1
    y = 1
    for i in range(1, n):
        x += 1
        y += 1
        if x * y > n:
            break
    print(x + y - 2)

=======
Suggestion 3

def main():
    N = int(input())
    if N == 2:
        print(1)
        return

    x = 1
    y = 1
    cnt = 0
    while x * y < N:
        if x <= y:
            x += 1
        else:
            y += 1
        cnt += 1
    print(cnt)

=======
Suggestion 4

def main():
    N = int(input())
    i = 1
    while i*(i+1) < N:
        i += 1
    print(i-1+i)

=======
Suggestion 5

def main():
    n = int(input())
    sum = 0
    for i in range(1, n):
        sum += i
        if sum >= n:
            print(sum - n + i)
            break

=======
Suggestion 6

def main():
    N = int(input())
    # N = 10000000019
    # N = 50
    # N = 10
    # N = 1000000000000000000
    #

=======
Suggestion 7

def main():
    N = int(input())
    x, y = 1, 1
    ans = 0
    while x != N:
        if (x+1)*(y+1) <= N:
            x += 1
            y += 1
        elif (x+1)*y <= N:
            x += 1
        elif x*(y+1) <= N:
            y += 1
        else:
            x -= 1
        ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    ans = 0
    ans = N - 1
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    # 1,1からの移動回数を求める
    # 1,1からの移動回数は、(N-1)の素因数を求める
    # 素因数の和が最小になるようにする
    # 2,2からの移動回数は、(N-1)の素因数の和から1を引いたもの
    # 2,2からの移動回数は、(N-1)の素因数の和から2を引いたもの
    # 3,3からの移動回数は、(N-1)の素因数の和から3を引いたもの
    # 4,4からの移動回数は、(N-1)の素因数の和から4を引いたもの
    # 5,5からの移動回数は、(N-1)の素因数の和から5を引いたもの
    # 6,6からの移動回数は、(N-1)の素因数の和から6を引いたもの
    # 7,7からの移動回数は、(N-1)の素因数の和から7を引いたもの
    # 8,8からの移動回数は、(N-1)の素因数の和から8を引いたもの
    # 9,9からの移動回数は、(N-1)の素因数の和から9を引いたもの
    # 10,10からの移動回数は、(N-1)の素因数の和から10を引いたもの
    # 11,11からの移動回数は、(N-1)の素因数の和から11を引いたもの
    # 12,12からの移動回数は、(N-1)の素因数の和から12を引いたもの
    # 13,13からの移動回数は、(N-1)
