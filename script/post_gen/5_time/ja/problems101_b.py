Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    sn = sum([int(x) for x in str(N)])
    if N % sn == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def getSumOfDigits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = int(n / 10)
    return sum

N = int(input())

=======
Suggestion 3

def main():
    n = int(input())
    s = 0
    for i in str(n):
        s += int(i)
    if n % s == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    n = int(input())
    if n % sum(list(map(int, list(str(n))))) == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    N = int(input())
    S = 0
    for i in str(N):
        S += int(i)
    if N % S == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    N = int(input())
    S = sum([int(i) for i in str(N)])
    if N % S == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    N = input()
    N = int(N)
    S = 0
    for i in str(N):
        S += int(i)
    if N % S == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    n = input()
    s = 0
    for i in n:
        s += int(i)
    if int(n) % s == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    n = int(input())
    s = 0
    for i in str(n):
        s += int(i)
    if n % s == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def main():
    n = input()
    s = sum([int(i) for i in n])
    if int(n) % s == 0:
        print('Yes')
    else:
        print('No')
