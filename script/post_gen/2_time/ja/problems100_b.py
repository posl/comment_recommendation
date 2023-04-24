Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    D, N = map(int, input().split())
    if D == 0:
        if N == 100:
            print(101)
        else:
            print(N)
    elif D == 1:
        if N == 100:
            print(10100)
        else:
            print(N*100)
    else:
        if N == 100:
            print(1010000)
        else:
            print(N*10000)

=======
Suggestion 2

def main():
    D, N = map(int, input().split())
    if D == 0:
        print(N)
    elif D == 1:
        print(N * 100)
    else:
        print(N * 10000)

=======
Suggestion 3

def main():
    d, n = map(int, input().split())
    if d == 0:
        print(n)
    elif d == 1:
        print(n * 100)
    else:
        print(n * 10000)

=======
Suggestion 4

def main():
    D, N = map(int, input().split())
    if N == 100:
        N += 1
    print(100 ** D * N)

=======
Suggestion 5

def main():
    # 入力
    D, N = map(int, input().split())
    # 出力
    if D == 0:
        if N == 100:
            print(101)
        else:
            print(N)
    elif D == 1:
        if N == 100:
            print(10100)
        else:
            print(N * 100)
    elif D == 2:
        if N == 100:
            print(1010000)
        else:
            print(N * 10000)

=======
Suggestion 6

def main():
    #入力
    D, N = map(int, input().split())
    #処理
    if D == 0:
        if N == 100:
            print(101)
        else:
            print(N)
    elif D == 1:
        if N == 100:
            print(10100)
        else:
            print(100 * N)
    else:
        if N == 100:
            print(1010000)
        else:
            print(10000 * N)

=======
Suggestion 7

def main():
    # A: 100で何回割り切れるか
    # B: N番目に小さいもの
    A, B = map(int, input().split())
    # 100でA回割り切れる数を求める
    ans = 100**A
    # 100でA回割り切れる数の中でB番目に小さい数を求める
    for i in range(1, B):
        ans += 100**A
    print(ans)
