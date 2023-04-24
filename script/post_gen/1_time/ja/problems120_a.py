Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    if a * c <= b:
        print(c)
    else:
        print(b // a)

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    if b // a >= c:
        print(c)
    else:
        print(b // a)

=======
Suggestion 3

def main():
    # input
    A, B, C = map(int, input().split())

    # compute
    ans = min(B//A, C)

    # output
    print(ans)

=======
Suggestion 4

def main():
    A, B, C = map(int, input().split())
    if B // A >= C:
        print(C)
    else:
        print(B // A)

=======
Suggestion 5

def solve():
    a, b, c = map(int, input().split())
    if b >= a * c:
        return c
    else:
        return b // a

print(solve())

=======
Suggestion 6

def main():
    # 自分の解答
    # A, B, C = map(int, input().split())
    # if A * C <= B:
    #     print(C)
    # else:
    #     print(B // A)
    # 他の人の解答
    A, B, C = map(int, input().split())
    print(min(B//A, C))

=======
Suggestion 7

def main():
    a, b, c = map(int, input().split())
    print(min(b//a, c))

=======
Suggestion 8

def solve():
    a,b,c = map(int, input().split())
    if a * c <= b:
        print(c)
    else:
        print(b//a)

=======
Suggestion 9

def main():
    # n = int(input())
    a, b, c = map(int, input().split())
    # s = input()
    # l = list(map(int, input().split()))
    # l = [list(map(int,input().split())) for _ in range(n)]
    if a * c <= b:
        print(c)
    else:
        print(b // a)

=======
Suggestion 10

def main():
    #入力
    a,b,c = map(int, input().split())

    #処理
    if a*c <= b:
        ans = c
    else:
        ans = b//a

    #出力
    print(ans)
