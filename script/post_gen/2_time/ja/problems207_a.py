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
    #入力
    A,B,C = map(int,input().split())
    #処理
    ans = max(A+B,A+C,B+C)
    #出力
    print(ans)

=======
Suggestion 6

def main():
    # A B Cを入力
    A, B, C = map(int, input().split())
    # AとBの合計値とAとCの合計値を比較し、大きい方の値を出力
    print(max(A + B, B + C, C + A))
