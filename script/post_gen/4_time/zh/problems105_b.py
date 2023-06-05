Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    if N % 4 == 0 or N % 7 == 0 or N % 11 == 0:
        print("Yes")
    elif N % 4 == 1 or N % 7 == 1 or N % 11 == 1:
        print("Yes")
    elif N % 4 == 2 or N % 7 == 2 or N % 11 == 2:
        print("Yes")
    elif N % 4 == 3 or N % 7 == 3 or N % 11 == 3:
        print("No")
    else:
        print("No")

=======
Suggestion 2

def main():
    n = int(input())
    for i in range(0, 26):
        for j in range(0, 16):
            if i*4 + j*7 == n:
                print("Yes")
                return
    print("No")
    return

=======
Suggestion 3

def main():
    n = int(input())
    for i in range(0, n // 4 + 1):
        for j in range(0, n // 7 + 1):
            if i * 4 + j * 7 == n:
                print('Yes')
                return
    print('No')

=======
Suggestion 4

def main():
    n = int(input())
    for i in range(0, n//4+1):
        for j in range(0, n//7+1):
            if (i*4 + j*7) == n:
                print("Yes")
                exit()
    print("No")

=======
Suggestion 5

def check(n):
    for i in range(0, n//4+1):
        for j in range(0, n//7+1):
            if i*4 + j*7 == n:
                print("Yes")
                return
    print("No")

=======
Suggestion 6

def main():
    N = int(input())
    if N%4 == 0 or N%7 == 0 or N%11 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    N = int(input())
    if N % 4 == 0 or N % 7 == 0 or N % 11 == 0 or N % 15 == 0 or N % 19 == 0 or N % 20 == 0 or N % 23 == 0 or N % 27 == 0 or N % 31 == 0 or N % 35 == 0 or N % 39 == 0 or N % 43 == 0 or N % 47 == 0 or N % 51 == 0 or N % 55 == 0 or N % 59 == 0 or N % 63 == 0 or N % 67 == 0 or N % 71 == 0 or N % 75 == 0 or N % 79 == 0 or N % 83 == 0 or N % 87 == 0 or N % 91 == 0 or N % 95 == 0 or N % 99 == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    N = int(input())
    if N % 4 == 0 or N % 7 == 0 or N % 11 == 0:
        print("Yes")
        return
    for i in range(1, N // 4 + 1):
        for j in range(1, N // 7 + 1):
            if 4 * i + 7 * j == N:
                print("Yes")
                return
    print("No")

=======
Suggestion 9

def main():
    n = int(input())
    for i in range(0, n+1, 4):
        if (n-i)%7 == 0:
            print('Yes')
            return
    print('No')

=======
Suggestion 10

def main():
    n = int(input())
    for i in range(0, n//4 + 1):
        for j in range(0, n//7 + 1):
            if 4*i + 7*j == n:
                print("Yes")
                return
    print("No")
