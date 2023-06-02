Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = input()
    if n % 2 == 0 and s[:int(n/2)] == s[int(n/2):]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    n = int(input())
    s = input()
    if n % 2 == 0 and s[0:n//2] == s[n//2:]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    n = int(input())
    s = input()
    if len(s) % 2 == 0:
        s1 = s[:len(s)//2]
        s2 = s[len(s)//2:]
        if s1 == s2:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 4

def check(s):
    if len(s) % 2 != 0:
        return False
    else:
        half = len(s) // 2
        if s[:half] == s[half:]:
            return True
        else:
            return False

n = int(input())
s = input()

=======
Suggestion 5

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
Suggestion 6

def problem145_b():
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
Suggestion 7

def main():
    n = int(input())
    s = input()
    flag = False
    for i in range(1, n):
        if s[:i] == s[i:]:
            flag = True
            break
    if flag:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    n = int(input())
    s = input()
    if n % 2 == 0 and s[0:n//2] == s[n//2:n]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
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
Suggestion 10

def judge(S):
    for i in range(1, len(S)):
        if len(S)%i == 0:
            if S[0:i]*(len(S)//i) == S:
                return True
    return False
