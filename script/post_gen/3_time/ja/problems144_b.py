Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    for i in range(1, 10):
        for j in range(1, 10):
            if i * j == N:
                print("Yes")
                return
    print("No")

=======
Suggestion 2

def main():
    N = int(input())
    for i in range(1, 10):
        if N % i == 0 and 1 <= N // i <= 9:
            print("Yes")
            return
    print("No")

=======
Suggestion 3

def main():
    n = int(input())
    for i in range(1, 10):
        if n % i == 0 and n // i <= 9:
            print("Yes")
            break
    else:
        print("No")

=======
Suggestion 4

def main():
    n = int(input())
    for i in range(1,10):
        if n % i == 0 and 1 <= n // i <= 9:
            print("Yes")
            return
    print("No")

=======
Suggestion 5

def main():
    N = int(input())
    for i in range(1, 10):
        if N % i == 0 and N // i < 10:
            print('Yes')
            return
    print('No')

=======
Suggestion 6

def main():
    n = int(input())
    for i in range(1,10):
        if n % i == 0 and n // i <= 9:
            print('Yes')
            return
    print('No')

=======
Suggestion 7

def main():
    N = int(input())
    for i in range(1,10):
        if N % i == 0 and N // i <= 9:
            print('Yes')
            break
    else:
        print('No')

=======
Suggestion 8

def solve():
    N = int(input())
    for i in range(1, 10):
        if N % i == 0:
            if N // i < 10:
                print('Yes')
                return
    print('No')
    return

=======
Suggestion 9

def check(num):
    for i in range(1,10):
        if num % i == 0 and num // i < 10:
            return True
    return False

n = int(input())
