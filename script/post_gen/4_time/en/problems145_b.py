Synthesizing 10/10 solutions

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
    if n % 2 == 0:
        if s[:n//2] == s[n//2:]:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

=======
Suggestion 3

def main():
    n = int(input())
    s = input()
    if s[:n//2] == s[n//2:]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

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
Suggestion 5

def main():
    n = int(input())
    s = input()
    if n % 2 == 1:
        print("No")
    else:
        if s[:n//2] == s[n//2:]:
            print("Yes")
        else:
            print("No")

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    if S[:N//2] == S[N//2:]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    n = int(input())
    s = input()
    if n%2 == 0 and s[:n//2] == s[n//2:]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

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
Suggestion 9

def main():
    n = int(input())
    s = input()
    if n%2 == 0:
        if s[:int(n/2)] == s[int(n/2):]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 10

def main():
    N = int(input())
    S = input()
    if N % 2 == 0:
        if S[0:int(N/2)] == S[int(N/2):]:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

main()
