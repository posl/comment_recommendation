Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max(b - c, d - a))

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max(max(a, b) - min(c, d), max(c, d) - min(a, b)))

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max(b-d, b-c, a-d, a-c))

=======
Suggestion 4

def main():
    #入力
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    #処理
    ans = max(a - d, b - c)
    #出力
    print(ans)

=======
Suggestion 5

def main():
    # 1行目を取得
    a, b = map(int, input().split())
    # 2行目を取得
    c, d = map(int, input().split())
    # x-yの最大値を出力
    print(max(b - c, d - a, b - d, c - a))
