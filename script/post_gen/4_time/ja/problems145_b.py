Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    if n % 2 == 0:
        if s[:n//2] == s[n//2:]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 2

def main():
    n = int(input())
    s = input()
    if s[0:n//2] == s[n//2:n]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    if S[0:N//2] == S[N//2:N]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    n = int(input())
    s = input()
    if n % 2 == 0:
        if s[0:n//2] == s[n//2:]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 5

def main():
    N = int(input())
    S = input()
    if N % 2 == 1:
        print("No")
    else:
        if S[0:N//2] == S[N//2:N]:
            print("Yes")
        else:
            print("No")

=======
Suggestion 6

def solve():
    n = int(input())
    s = input()
    if s[0:n//2] == s[n//2:n]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    if len(S) % 2 == 0:
        if S[:int(len(S)/2)] == S[int(len(S)/2):]:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

=======
Suggestion 8

def check(s):
    n = len(s)
    if n % 2 != 0:
        return False
    m = n // 2
    if s[:m] == s[m:]:
        return True
    return False

=======
Suggestion 9

def check_double_string(n, s):
    if n % 2 != 0:
        return False

    half = int(n/2)
    if s[0:half] == s[half:n]:
        return True
    else:
        return False

n = int(input())
s = input()
