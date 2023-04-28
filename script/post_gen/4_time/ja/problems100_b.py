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
            print(100 * N)
    else:
        if N == 100:
            print(1010000)
        else:
            print(10000 * N)

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
            print(N * 100)
    else:
        if N == 100:
            print(1010000)
        else:
            print(N * 10000)

=======
Suggestion 3

def main():
    D,N = map(int, input().split())
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

main()

=======
Suggestion 4

def main():
    d, n = map(int, input().split())
    if n == 100:
        n = 101
    print(100**d * n)

=======
Suggestion 5

def main():
    d,n = map(int, input().split())
    if n == 100:
        n += 1
    print(100**d * n)

=======
Suggestion 6

def main():
    d,n = map(int,input().split())
    if n == 100:
        n += 1
    print(n*100**d)

=======
Suggestion 7

def main():
    # データ入力
    d, n = map(int, input().split())
    # 処理
    if d == 0:
        if n == 100:
            n = 101
        print(n)
    elif d == 1:
        if n == 100:
            n = 101
        print(n * 100)
    elif d == 2:
        if n == 100:
            n = 101
        print(n * 10000)

=======
Suggestion 8

def main():
    D,N = map(int,input().split())
    if N == 100:
        N = 101
    print(N * (100 ** D))

=======
Suggestion 9

def main():
    print("Hello World!")
