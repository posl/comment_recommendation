Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # input
    A, B = map(int, input().split())

    # compute

    # output
    print(max(A+A-1, A+B, B+B-1))

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    if A == B:
        print(A * 2)
    else:
        print(max(A, B) * 2 - 1)

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if a == b:
        print(2 * a)
    else:
        print(max(2 * a - 1, 2 * b - 1, a + b))

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    if A == B:
        print(A + B)
    else:
        print(max(A + A - 1, B + B - 1, A + B))

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    print(max(a + a - 1, b + b - 1, a + b))

=======
Suggestion 6

def main():
    # input
    a, b = map(int, input().split())

    # compute
    ans = max(a+a-1, a+b, b+b-1)

    # output
    print(ans)

=======
Suggestion 7

def main():
    A, B = map(int, input().split())

    if A >= B:
        print(A + max(A - 1, B))
    else:
        print(B + max(A, B - 1))

=======
Suggestion 8

def solve():
    a, b = map(int, input().split())
    if a == b:
        return a + b
    else:
        return max(a + a - 1, b + b - 1, a + b)

print(solve())

=======
Suggestion 9

def main():
    # 標準入力から A, B を取得する
    A, B = map(int, input().split())
    # ボタンを 2 回押す場合
    ans = max(A + A - 1, B + B - 1)
    # ボタンを 1 回ずつ押す場合
    ans = max(ans, A + B)
    # 結果を出力する
    print(ans)
