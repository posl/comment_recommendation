Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    if N % 9 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    N = input()
    if int(N) % 9 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    N = input()
    N = int(N)
    sum = 0
    while N > 0:
        sum += N % 10
        N = N // 10
    if sum % 9 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    n = input()
    n = list(n)
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    if sum%9 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    N = input()
    N = int(N)
    N = str(N)
    sum = 0
    for i in range(len(N)):
        sum += int(N[i])
    if sum % 9 == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    n = input()
    print("Yes" if sum([int(i) for i in n]) % 9 == 0 else "No")

=======
Suggestion 7

def is_multiple_of_9(n):
    if n % 9 == 0:
        return True
    else:
        return False

=======
Suggestion 8

def solve():
    N = int(input())
    print("Yes" if N % 9 == 0 else "No")

=======
Suggestion 9

def problem176_b():
    n = input()
    n = int(n)
    if n % 9 == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def solve():
    n = input()
    n = int(n)
    print("Yes" if n%9 == 0 else "No")
solve()
