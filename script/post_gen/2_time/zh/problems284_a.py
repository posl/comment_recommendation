Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        print(s[n-i-1])

=======
Suggestion 2

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.reverse()
    for i in range(N):
        print(S[i])

=======
Suggestion 3

def main():
    # 读取输入
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    # 逆序输出
    for i in range(N):
        print(S[N-i-1])

=======
Suggestion 4

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    for i in range(N):
        print(S[N-1-i])

=======
Suggestion 5

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.reverse()
    for i in range(n):
        print(s[i])

=======
Suggestion 6

def reverse_print():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        print(s[n - i - 1])

=======
Suggestion 7

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())

    for i in range(n):
        print(s[n-1-i])
