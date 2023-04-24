Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    for i in range(K):
        if N % 200 == 0:
            N = N // 200
        else:
            N = int(str(N) + "200")
    print(N)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    for i in range(k):
        if n % 200 == 0:
            n = n // 200
        else:
            n = int(str(n) + '200')
    print(n)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    for i in range(K):
        if N % 200 == 0:
            N //= 200
        else:
            N = int(str(N) + '200')
    print(N)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    for i in range(K):
        if N%200 == 0:
            N = N//200
        else:
            N = int(str(N) + '200')
    print(N)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    for i in range(1, K+1):
        if N % 200 == 0:
            N //= 200
        else:
            N = int(str(N) + "200")
    print(N)

=======
Suggestion 6

def main():
    # 入力
    n,k = map(int,input().split())
    # 処理
    for i in range(k):
        if n%200==0:
            n=n//200
        else:
            n=int(str(n)+"200")
    # 出力
    print(n)

=======
Suggestion 7

def main():
    # 整数の入力
    N, K = map(int, input().split())
    # 文字列の入力
    #S = input()
    # 出力
    for i in range(K):
        if N % 200 == 0:
            N = N // 200
        else:
            N = int(str(N) + "200")
    print(N)
