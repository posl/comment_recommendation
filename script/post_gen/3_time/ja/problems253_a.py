Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b, c = map(int, input().split())
    if (a <= b <= c) or (c <= b <= a):
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    a, b, c = map(int, input().split())
    if a <= b <= c or c <= b <= a:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    a, b, c = map(int, input().split())
    if a < b < c or c < b < a:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    a, b, c = map(int, input().split())
    if b == sorted([a, b, c])[1]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    a, b, c = map(int, input().split())
    if b == sorted([a, b, c])[1]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    a, b, c = map(int, input().split())
    if b >= min(a, c) and b <= max(a, c):
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    # 入力
    a, b, c = map(int, input().split())

    # 処理
    if a < b and b < c or c < b and b < a:
        print("Yes")
    else:
        print("No")
