Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def is_multiple_of_9(str):
    sum = 0
    for i in range(len(str)):
        sum += int(str[i])
    return sum % 9 == 0

=======
Suggestion 2

def main():
    N = input()
    n = 0
    for i in N:
        n += int(i)
    if n % 9 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    n = input()
    n_list = list(n)
    n_list = list(map(int, n_list))
    sum_n = sum(n_list)
    if sum_n % 9 == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    n = input()
    if int(n) % 9 == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    n = int(input())
    if n % 9 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def is_multiple_of_9(n):
    if n % 9 == 0:
        return True
    else:
        return False

=======
Suggestion 7

def main():
    n = input()
    n = int(n)
    if n % 9 == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def is_multiple_of_9(s):
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
    if sum % 9 == 0:
        return True
    else:
        return False

=======
Suggestion 9

def check(n):
    s = str(n)
    l = len(s)
    sum = 0
    for i in range(l):
        sum += int(s[i])
    if sum % 9 == 0:
        return True
    else:
        return False
