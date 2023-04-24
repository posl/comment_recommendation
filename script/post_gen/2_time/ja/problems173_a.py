Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    print(1000 - N % 1000 if N % 1000 != 0 else 0)

=======
Suggestion 2

def main():
    n = int(input())
    print(1000 - n % 1000 if n % 1000 != 0 else 0)

=======
Suggestion 3

def main():
    N = int(input())
    print((N // 1000 + 1) * 1000 - N)

=======
Suggestion 4

def main():
    # 入力
    N = int(input())
    # 処理
    ans = 1000 - N % 1000
    if ans == 1000:
        ans = 0
    # 出力
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    print(1000 - N % 1000)

=======
Suggestion 6

def main():
    N = int(input())
    print(N%1000)
