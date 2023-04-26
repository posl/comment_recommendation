Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    print(max(a+b, b+c, c+a))

=======
Suggestion 2

def main():
    A, B, C = map(int, input().split())
    print(max(A+B, B+C, C+A))

=======
Suggestion 3

def main():
    A,B,C = map(int,input().split())
    print(max(A+B,A+C,B+C))

=======
Suggestion 4

def main():
    a,b,c = map(int,input().split())
    print(max(a+b,a+c,b+c))

=======
Suggestion 5

def main():
    A,B,C = map(int, input().split())
    print(A+B+C - min(A,B,C))

=======
Suggestion 6

def main():
    # 3つの整数を入力
    A, B, C = map(int, input().split())
    # A,B,Cの合計値を出力
    print(A+B+C-max(A,B,C))

=======
Suggestion 7

def main(): #main関数を定義
    A, B, C = map(int, input().split()) #map関数を使って、入力を整数に変換して、それぞれA,B,Cに代入
    print(max(A+B,A+C,B+C)) #max関数を使って、A+B,A+C,B+Cの中で最大の値を出力
