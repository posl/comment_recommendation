Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = input()
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    if sum % 9 == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    #n = int(input())
    n = input()
    #print(n)
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    if sum % 9 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    N = int(input())
    if N%9 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    N = input()
    sum = 0
    for i in N:
        sum += int(i)
    if sum % 9 == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    n = input()
    total = 0
    for i in n:
        total += int(i)
    if total % 9 == 0:
        print('Yes')
    else:
        print('No')

main()

=======
Suggestion 6

def solve():
    n = input()
    if int(n)%9==0:
        print("Yes")
    else:
        print("No")

solve()

=======
Suggestion 7

def isMultipleOf9(n):
    if (n == 0 or n == 9):
        return True
    if (n < 9):
        return False
    return isMultipleOf9(int(n/9) - int(n%9))

n = input()

=======
Suggestion 8

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
Suggestion 9

def is_9_multiple(n):
    sum = 0
    for i in n:
        sum += int(i)
    if sum % 9 == 0:
        return True
    else:
        return False
