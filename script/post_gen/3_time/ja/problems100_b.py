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
        if N == 100:
            print(101)
        else:
            print(N)
    elif D == 1:
        if N == 100:
            print(10100)
        else:
            print(N*100)
    elif D == 2:
        if N == 100:
            print(1010000)
        else:
            print(N*10000)

=======
Suggestion 3

def main():
    d, n = map(int, input().split())

    if d == 0:
        if n == 100:
            print(101)
        else:
            print(n)
    elif d == 1:
        if n == 100:
            print(10100)
        else:
            print(n*100)
    elif d == 2:
        if n == 100:
            print(1010000)
        else:
            print(n*10000)
    else:
        print(0)

=======
Suggestion 4

def main():
    D, N = map(int, input().split())
    if N == 100:
        print((100**D)*101)
    else:
        print((100**D)*N)

=======
Suggestion 5

def main():
    d,n = map(int,input().split())
    if n == 100:
        n += 1
    print(100**d*n)

=======
Suggestion 6

def cal_100(d, n):
    if d == 0:
        return n
    elif d == 1:
        return 100 * n
    else:
        return 10000 * n

d, n = map(int, input().split())
print(cal_100(d, n))

=======
Suggestion 7

def main():
    d,n = map(int, input().split())
    if n == 100:
        n += 1
    print(100**d*n)

main()

=======
Suggestion 8

def main():
    # 標準入力から入力値を取得する
    d, n = map(int, input().split())
    # 100 でちょうど d 回割り切れる整数のリストを作成する
    num_list = [100 ** d * i for i in range(1, 101)]
    # num_list の n 番目の要素を出力する
    print(num_list[n - 1])
