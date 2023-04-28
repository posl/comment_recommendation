Synthesizing 10/10 solutions

=======
Suggestion 1

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

def solve():
    n = input()
    s = 0
    for c in n:
        s += int(c)
    if s % 9 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    n = int(input())
    s = 0
    for i in str(n):
        s += int(i)
    if s % 9 == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    n = input()
    sum = 0
    for i in n:
        sum += int(i)
    if sum % 9 == 0:
        print("Yes")
    else:
        print("No")
main()

=======
Suggestion 7

def main():
    N = input()
    sum = 0
    for i in N:
        sum += int(i)
    if sum % 9 == 0:
        print('Yes')
    else:
        print('No')

main()

=======
Suggestion 8

def main():
    n = int(input())
    if n % 9 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    N = input()
    if int(N) % 9 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    n = input()
    n = list(n)
    n = list(map(int, n))
    if sum(n) % 9 == 0:
        print('Yes')
    else:
        print('No')
