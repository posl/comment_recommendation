Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    X, A = map(int, input().split())
    if X < A:
        print(0)
    else:
        print(10)

=======
Suggestion 2

def main():
    x, a = map(int, input().split())
    if x < a:
        print(0)
    else:
        print(10)

=======
Suggestion 3

def main():
    X, A = map(int, input().split())
    if X < A:
        print("0")
    elif X >= A:
        print("10")

=======
Suggestion 4

def main():
    # 入力
    X, A = map(int, input().split())
    # 出力
    if X < A:
        print(0)
    else:
        print(10)

=======
Suggestion 5

def main():
    x, a = map(int, input().split())
    print(0 if x < a else 10)
