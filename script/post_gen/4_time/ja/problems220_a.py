Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    for i in range(a, b+1):
        if i % c == 0:
            print(i)
            return
    print(-1)

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    for i in range(a, b+1):
        if i % c == 0:
            print(i)
            break
    else:
        print(-1)

=======
Suggestion 3

def main():
    A, B, C = map(int, input().split())
    for i in range(A, B+1):
        if i % C == 0:
            print(i)
            break
    else:
        print(-1)

=======
Suggestion 4

def main():
    a,b,c = map(int,input().split())
    for i in range(a,b+1):
        if i % c == 0:
            print(i)
            break
        elif i == b:
            print(-1)

=======
Suggestion 5

def main():
    a,b,c = map(int,input().split())
    for i in range(a,b+1):
        if i%c == 0:
            print(i)
            exit()
    print(-1)

=======
Suggestion 6

def solve():
    # 整数 1 つ
    #a = int(input())
    # スペース区切りの整数の入力
    #b, c = map(int, input().split())
    # 文字列 1 つ
    #s = input()
    # スペース区切りの文字列の入力
    #t, u = input().split()
    # 出力
    #print("{} {}".format(a+b+c, s))
    #print("{} {}".format(a*b*c, s))
    #prin

=======
Suggestion 7

def main():
    a, b, c = map(int, input().split())
    if a % c == 0:
        print(a)
    else:
        print(a + c - (a % c))

=======
Suggestion 8

def main():
    # A,B,Cの値を受け取る
    a,b,c = map(int, input().split())
    # A以上B以下のCの倍数を求める
    if a % c == 0:
        print(a)
    else:
        print((a // c + 1) * c)
