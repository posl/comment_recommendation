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
    num = int(input())
    str = input()
    if num % 2 == 0:
        half = int(num / 2)
        if str[0:half] == str[half:]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 3

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
Suggestion 4

def main():
    n = int(input())
    s = input()
    if n % 2 == 1:
        print('No')
    else:
        if s[:int(n/2)] == s[int(n/2):]:
            print('Yes')
        else:
            print('No')

=======
Suggestion 5

def main():
    N = int(input())
    S = input()
    if S[0:N//2] == S[N//2:N]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    flag = False
    for i in range(1, N):
        if S[:i] == S[i:]:
            flag = True
            break
    if flag:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    if N % 2 == 0:
        if S[:N//2] == S[N//2:]:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

=======
Suggestion 8

def main():
    n = int(input())
    s = input()
    if s[0:n//2] == s[n//2:n]:
        print('Yes')
    else:
        print('No')
