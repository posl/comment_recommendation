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
    n = input()
    n = list(n)
    sum = 0
    for i in n:
        sum += int(i)
    if sum % 9 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    n = input()
    sum = 0
    for i in n:
        sum += int(i)
    if sum % 9 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    n = input()
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    if sum % 9 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def is_multiple_of_9(s):
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
    if sum % 9 == 0:
        return True
    else:
        return False

=======
Suggestion 6

def main():
    N = input()
    sum = 0
    for i in range(len(N)):
        sum += int(N[i])
    if sum % 9 == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

n = int(input())

=======
Suggestion 8

def solve():
    n = input()
    if int(n) % 9 == 0:
        print("Yes")
    else:
        print("No")
