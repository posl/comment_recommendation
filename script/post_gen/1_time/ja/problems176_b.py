Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = input()
    sum = 0
    for i in range(len(N)):
        sum += int(N[i])

    if sum % 9 == 0:
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

def is_multiple_of_9(s):
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
    return sum % 9 == 0

=======
Suggestion 4

def solve():
    import sys
    readline = sys.stdin.buffer.readline
    n = readline().rstrip().decode('utf-8')
    if int(n)%9==0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def is_multiple_of_9(n):
    if n % 9 == 0:
        return True
    else:
        return False

=======
Suggestion 6

def solve():
    N = input()
    if int(N)%9==0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def check9(n):
    if n % 9 == 0:
        return True
    else:
        return False

=======
Suggestion 8

def solve():
    #coding:utf-8
    n = input()
    if n == '0':
        print('Yes')
        return
    if len(n) == 1:
        print('No')
        return
    num = 0
    for i in n:
        num += int(i)
    if num % 9 == 0:
        print('Yes')
    else:
        print('No')
    return

=======
Suggestion 9

def nine_multiple(N):
    if N % 9 == 0:
        return "Yes"
    else:
        return "No"
