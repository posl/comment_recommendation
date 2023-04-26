Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = input()
    if N == N[::-1]:
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 2

def main():
    N = input()
    if N == N[::-1]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    N = input()
    if N == N[::-1]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    n = input()
    if n == n[::-1]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    N = int(input())
    N_str = str(N)
    N_str_reverse = N_str[::-1]
    if N_str == N_str_reverse:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    N = int(input())
    N_str = str(N)
    N_str_rev = N_str[::-1]
    if N_str == N_str_rev:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    N = input()
    N = N[::-1]
    N = N.lstrip("0")
    N2 = N[::-1]
    if N == N2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def is_palindrome(n):
    return str(n) == str(n)[::-1]

=======
Suggestion 9

def is_palindrome(s):
    return s == s[::-1]
