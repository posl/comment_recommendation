Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    if s[:n//2] == s[n//2:]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

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
Suggestion 3

def solve():
    n = int(input())
    s = input()
    if n % 2 == 0:
        if s[:n//2] == s[n//2:]:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    if N % 2 == 0:
        if S[0:N//2] == S[N//2:N]:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

=======
Suggestion 5

def main():
    N = int(input())
    S = input()
    if S == S[:N//2]*2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    n = int(input())
    s = input()
    print('Yes' if s[:n//2] == s[n//2:] else 'No')

=======
Suggestion 7

def main():
    N = input()
    S = input()
    if(N % 2 == 0):
        if(S[0:N/2] == S[N/2:N]):
            print("Yes")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 8

def isDouble(s):
    if len(s) % 2 != 0:
        return False
    else:
        s1 = s[:len(s)//2]
        s2 = s[len(s)//2:]
        if s1 == s2:
            return True
        else:
            return False

N = int(input())
S = input()

=======
Suggestion 9

def judge(s):
    for i in range(1, len(s)):
        if s == s[i:] + s[:i]:
            return True
    return False

n = int(input())
s = input()
print("Yes" if judge(s) else "No")

=======
Suggestion 10

def judge_repeat_string(s):
    if len(s) % 2 != 0:
        return False
    else:
        mid = len(s) // 2
        if s[:mid] == s[mid:]:
            return True
        else:
            return False
