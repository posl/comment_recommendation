Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    print(A / (A + B), B / (A + B))

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    d = (A**2 + B**2)**0.5
    print(A/d, B/d)

=======
Suggestion 3

def main():
    #入力
    A, B = map(int, input().split())
    #A, B = 3, 4
    #A, B = 1, 0
    #A, B = 246, 402

    #処理
    X = A / (A**2 + B**2)**0.5
    Y = B / (A**2 + B**2)**0.5

    #出力
    print(X, Y)

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    if A == 0:
        print(0, 1)
    elif B == 0:
        print(1, 0)
    else:
        print(B / (A**2 + B**2)**0.5, A / (A**2 + B**2)**0.5)

=======
Suggestion 5

def main():
    a,b = map(int,input().split())
    x = a/(a+b)
    y = b/(a+b)
    print(x,y)

=======
Suggestion 6

def main():
    A,B = map(int,input().split())
    G = (A*A+B*B)**0.5
    print(A/G,B/G)

=======
Suggestion 7

def main():
    # A,Bを取得
    A,B = map(int,input().split())
    # A,Bの最大公約数を取得
    gcd = GCD(A,B)
    # 最大公約数で割った時のA,Bの値を出力
    print(A/gcd,B/gcd)

=======
Suggestion 8

def main():
    A,B = map(int, input().split())
    #print(A,B)
    print(A/(A+B),B/(A+B))
