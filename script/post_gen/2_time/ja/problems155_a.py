Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    if a == b or b == c or c == a:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    if (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    A, B, C = map(int, input().split())
    if A == B and A != C:
        print("Yes")
    elif B == C and B != A:
        print("Yes")
    elif C == A and C != B:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    A, B, C = map(int, input().split())
    if A == B or A == C or B == C:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    a, b, c = map(int, input().split())
    if a == b and b != c:
        print("Yes")
    elif a == c and c != b:
        print("Yes")
    elif b == c and c != a:
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 6

def main():
    a, b, c = map(int, input().split())
    if a == b or b == c or a == c:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    # 入力
    A, B, C = map(int, input().split())
    # 処理
    if A == B or A == C or B == C:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    # A, B, C = map(int, input().split())
    A, B, C = map(int, input().split())
    if A == B:
        if B == C:
            print("No")
        else:
            print("Yes")
    elif B == C:
        print("Yes")
    elif A == C:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    # 1行目の入力
    A, B, C = map(int, input().split())
    # 3つの整数が全て同じかどうか
    if A == B == C:
        print("No")
    # 3つの整数のうち、2つが同じかどうか
    elif A == B or A == C or B == C:
        print("Yes")
    # 3つの整数が全て異なる場合
    else:
        print("No")
