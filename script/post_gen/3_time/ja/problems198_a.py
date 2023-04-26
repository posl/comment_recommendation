Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    if n == 1:
        print(0)
    elif n == 2:
        print(1)
    else:
        print(n - 1)

main()

=======
Suggestion 2

def main():
    N = int(input())
    if N == 1:
        print(0)
    else:
        print(N-1)

=======
Suggestion 3

def main():
    N = int(input())
    #print(N)
    if N == 1:
        print(0)
    else:
        print(2**(N-1))

=======
Suggestion 4

def main():
    N = int(input())
    # お菓子が0個の場合は0通り
    if N == 0:
        print(0)
    else:
        # お菓子が1個以上の場合は、N個のうち1個以上を取る方法がN通りある
        print(N)

=======
Suggestion 5

def main():
    n = int(input())
    print(int(n*(n-1)/2))

=======
Suggestion 6

def main():
    # 入力
    N = int(input())
    # 出力
    print(N//2)

=======
Suggestion 7

def main():
    n = int(input())
    print(n // 2)

=======
Suggestion 8

def main():
    N = int(input())
    print(2 ** (N - 1))

=======
Suggestion 9

def main():
  n = int(input())
  print(n*(n-1)//2)

=======
Suggestion 10

def main():
    #入力
    N = int(input())

    #処理
    #A君は1個以上、B君はN-1個以上取る
    #A君が1個取るとき、B君はN-1個取る
    #A君が2個取るとき、B君はN-2個取る
    #A君が3個取るとき、B君はN-3個取る
    #A君が4個取るとき、B君はN-4個取る
    #A君が5個取るとき、B君はN-5個取る
    #A君が6個取るとき、B君はN-6個取る
    #A君が7個取るとき、B君はN-7個取る
    #A君が8個取るとき、B君はN-8個取る
    #A君が9個取るとき、B君はN-9個取る
    #A君が10個取るとき、B君はN-10個取る
    #A君が11個取るとき、B君はN-11個取る
    #A君が12個取るとき、B君はN-12個取る
    #A君が13個取るとき、B君はN-13個取る
    #A君が14個取るとき、B君はN-14個取る
    #A君が15個取るとき、B君はN-15個取る

    #A君が1個取るとき、B君はN-1個取る
    #A君が2個取るとき、B君はN-2個取る
    #A君が3個取るとき、B
