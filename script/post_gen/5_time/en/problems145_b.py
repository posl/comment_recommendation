Synthesizing 10/10 solutions (Duplicates hidden)

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
Suggestion 3

def main():
    N = int(input())
    S = input()
    if N % 2 == 0 and S[:N//2] == S[N//2:]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    if S[:N//2] == S[N//2:]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    N = int(input())
    S = input()
    if S[0:int(N/2)] == S[int(N/2):]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    if N%2 == 0:
        if S[0:N//2] == S[N//2:N]:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

=======
Suggestion 7

def main():
    N = int(input())
    S = input()

    if N%2 == 0:
        if S[:int(N/2)] == S[int(N/2):]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 8

def main():
    n = int(input())
    s = input()
    if s[:n//2]*2 == s:
        print("Yes")
    else:
        print("No")
