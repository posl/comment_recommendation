Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def problem105_b():
    N = int(input())
    if N % 4 == 0 or N % 7 == 0 or N % 11 == 0:
        print("Yes")
    elif N % 4 == 1 or N % 7 == 1 or N % 11 == 1:
        print("No")
    else:
        print("Yes")

=======
Suggestion 2

def main():
    n = int(input())
    if n % 4 == 0 or n % 7 == 0 or n % 11 == 0:
        print("Yes")
    elif n % 4 % 7 == 0 or n % 4 % 11 == 0 or n % 7 % 11 == 0:
        print("Yes")
    elif n % 4 % 7 % 11 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    n = int(input())
    for i in range(0, n//4+1):
        for j in range(0, n//7+1):
            if 4*i+7*j == n:
                print('Yes')
                return
    print('No')

=======
Suggestion 4

def main():
    n = int(input())
    for i in range(0, n+1, 4):
        if (n-i)%7==0:
            print("Yes")
            exit()
    print("No")

=======
Suggestion 5

def main():
    N = int(input())
    if N % 4 == 0:
        print('Yes')
    elif N % 7 == 0:
        print('Yes')
    elif N % 11 == 0:
        print('Yes')
    elif N % 4 == 3:
        print('Yes')
    elif N % 7 == 3:
        print('Yes')
    elif N % 11 == 3:
        print('Yes')
    elif N % 4 == 7:
        print('Yes')
    elif N % 7 == 7:
        print('Yes')
    elif N % 11 == 7:
        print('Yes')
    elif N % 4 == 11:
        print('Yes')
    elif N % 7 == 11:
        print('Yes')
    elif N % 11 == 11:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    n = int(input())
    if n % 7 == 0 or n % 4 == 0 or n % 11 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    N = int(input())
    if N % 4 == 0:
        print("Yes")
    elif N % 7 == 0:
        print("Yes")
    elif N % 11 == 0:
        print("Yes")
    elif N % 4 + N % 7 == 11:
        print("Yes")
    elif N % 4 + N % 11 == 7:
        print("Yes")
    elif N % 7 + N % 11 == 4:
        print("Yes")
    elif N % 4 + N % 7 + N % 11 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def solve():
    N = int(input())
    for i in range(0, N//4 + 1):
        for j in range(0, N//7 + 1):
            if i*4 + j*7 == N:
                print("Yes")
                exit()
    print("No")

=======
Suggestion 9

def main():
    n = int(input())
    for i in range(0, n//4+1):
        for j in range(0, n//7+1):
            if i*4+j*7 == n:
                print("Yes")
                exit()
    print("No")
    return
