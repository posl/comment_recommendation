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
    print(max([b - c, b - d, a - c, a - d]))

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(max(a - d, b - c))

=======
Suggestion 4

def main():
    a,b = map(int, input().split())
    c,d = map(int, input().split())
    print(max([b-d, b-c, a-d, a-c]))

=======
Suggestion 5

def main():
    # 入力
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    
    # 処理
    ans = max(abs(a - d), abs(b - c), abs(a - c), abs(b - d))
    
    # 出力
    print(ans)
