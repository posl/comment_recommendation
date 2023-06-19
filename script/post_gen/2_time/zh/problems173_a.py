Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve(n):
    return 1000 - n % 1000 if n % 1000 != 0 else 0

=======
Suggestion 2

def change(N):
    if N % 1000 == 0:
        return 0
    else:
        return 1000 - N % 1000

=======
Suggestion 3

def main():
    # 读取输入
    n = int(input())
    # 计算结果
    ans = 1000 - n % 1000
    # 输出结果
    print(ans)

=======
Suggestion 4

def solve():
    n = int(input())
    print(1000 - n%1000)

=======
Suggestion 5

def change(n):
    return 1000 - n%1000

=======
Suggestion 6

def main():
    N = int(input())
    print(1000 - N % 1000)

=======
Suggestion 7

def main():
    n = int(input())
    print(1000 - n % 1000)

main()

=======
Suggestion 8

def change(N):
    return 1000 - N % 1000

=======
Suggestion 9

def main():
    n = int(input())
    print(1000 - n % 1000)
