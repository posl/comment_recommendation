Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

def main():
    N = int(input())
    S = input()
    if N % 2 != 0:
        print('No')
    else:
        half = int(N/2)
        if S[:half] == S[half:]:
            print('Yes')
        else:
            print('No')

=======
Suggestion 3

def check(s):
    n = len(s)
    for i in range(n//2):
        if s[:i+1] == s[i+1:2*i+2]:
            return True
    return False

n = int(input())
s = input()

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    T = S[:int(N/2)]
    if S == T + T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def is_double_copy_string(string):
    string_len = len(string)
    if string_len % 2 != 0:
        return False
    else:
        string_half_len = int(string_len / 2)
        if string[0:string_half_len] == string[string_half_len:]:
            return True
        else:
            return False

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    if N % 2 == 0:
        if S[:int(N/2)] == S[int(N/2):]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 7

def main():
    n = int(input())
    s = input()
    if s[:n//2] == s[n//2:]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    N = int(input())
    S = input()
    if N % 2 == 1:
        print("No")
        return
    else:
        if S[0:N//2] == S[N//2:N]:
            print("Yes")
        else:
            print("No")

=======
Suggestion 9

def main():
    N = int(input())
    S = input()
    if N % 2 == 0 and S[:N//2] == S[N//2:]:
        print("Yes")
    else:
        print("No")
