Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    if A <= B * 2:
        print(0)
    else:
        print(A - B * 2)

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    if A >= B * 2:
        print(A - B * 2)
    else:
        print(0)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    print(max(0, a - 2 * b))

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    print(max(0, A - 2 * B))

=======
Suggestion 5

def main():
    a,b = map(int,input().split())
    if a <= b*2:
        print(0)
    else:
        print(a-b*2)

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    print(max(0, a - b * 2))

=======
Suggestion 7

def main():
    a,b = map(int,input().split())
    if a > 2*b:
        print(a-2*b)
    else:
        print(0)

=======
Suggestion 8

def main():
    a, b = map(int, input().split())
    print(a - 2 * b if 2 * b <= a else 0)

=======
Suggestion 9

def main():
    # A:窓の横幅,B:カーテンの横幅
    A, B = map(int, input().split())
    # 窓の横幅がカーテンの横幅より短い場合
    if A < B:
        print(0)
    # 窓の横幅がカーテンの横幅より長い場合
    else:
        print(A - B)

=======
Suggestion 10

def main():
    A, B = map(int, input().split())
    print(A - (B + B))
