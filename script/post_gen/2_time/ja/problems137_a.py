Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    print(max(a + b, a - b, a * b))

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    print(max(A + B, A - B, A * B))

=======
Suggestion 3

def main():
    # A, B を取得
    A, B = map(int, input().split())
    # A + B, A - B, A * B の中で最大の数を出力
    print(max(A + B, A - B, A * B))
