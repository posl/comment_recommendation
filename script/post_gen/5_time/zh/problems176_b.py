Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    if (n % 9 == 0):
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

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
Suggestion 3

def is_multiple_of_nine(n):
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    return sum % 9 == 0

=======
Suggestion 4

def is_9_multiple(n):
    if n == 0:
        return True
    if n % 9 == 0:
        return True
    else:
        return False

=======
Suggestion 5

def main():
    n = input()
    n = list(n)
    n = list(map(int, n))
    if sum(n) % 9 == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    s = input()
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
    if sum % 9 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

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
Suggestion 8

def main():
    n = int(input())
    if n % 9 == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    n = int(input())
    if n % 9 == 0:
        print("Yes")
    else:
        print("No")
