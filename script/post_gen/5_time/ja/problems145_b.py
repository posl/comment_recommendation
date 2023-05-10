Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    if n % 2 == 0:
        if s[0:n//2] == s[n//2:n]:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

=======
Suggestion 2

def is_double_string(s):
    if len(s) % 2 == 1:
        return False
    else:
        n = len(s) // 2
        return s[:n] == s[n:]

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    if N % 2 == 0:
        if S[:N//2] == S[N//2:]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 4

def check(s):
    if len(s) % 2 == 1:
        return False
    else:
        half = len(s) // 2
        if s[:half] == s[half:]:
            return True
        else:
            return False

N = int(input())
S = input()

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    if n % 2 == 0 and s[0:n//2] == s[n//2:n]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    n = int(input())
    s = input()
    if s[0:int(n/2)] == s[int(n/2):n]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    # 標準入力受け取り
    n = int(input())
    s = input()

    # 文字列を二回繰り返したものがあるかを判定
    if s[:n//2] == s[n//2:]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    n = int(input())
    s = input()
    if s[:n//2] == s[n//2:]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    n = int(input())
    s = input()
    if s[:n//2]*2 == s:
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def main():
    n = int(input())
    s = input()
    if s[:n//2] == s[n//2:]:
        print("Yes")
    else:
        print("No")
