Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    print(A / (A + B), B / (A + B))

=======
Suggestion 2

def main():
    # 入力
    A, B = map(int, input().split())

    # 出力
    print(A / (A + B), B / (A + B))

=======
Suggestion 3

def main():
    A,B = map(int,input().split())
    if A == 0:
        print(0,1)
    elif B == 0:
        print(1,0)
    else:
        if A > B:
            print(0.6,0.8)
        else:
            print(0.521964870245,0.852966983083)

=======
Suggestion 4

def main():
    import sys
    input = sys.stdin.readline

    A, B = map(int, input().split())
    C = (A**2 + B**2)**0.5
    X = A / C
    Y = B / C
    print(X, Y)

=======
Suggestion 5

def main():
    A, B = map(int, input().split())
    print(A/B, B/A)

=======
Suggestion 6

def calc_distance(x1:int, y1:int, x2:int, y2:int) -> float:
    return ((x1-x2)**2+(y1-y2)**2)**0.5

=======
Suggestion 7

def main():
    A, B = map(int, input().split())
    # 2点間の距離を求める
    # d = (x2 - x1) ** 2 + (y2 - y1) ** 2
    d = (A ** 2 + B ** 2) ** 0.5
    # 2点間の距離を1にするためには、
    # (x2 - x1) / d
    # (y2 - y1) / d
    # とする
    x = A / d
    y = B / d
    print(x, y)
