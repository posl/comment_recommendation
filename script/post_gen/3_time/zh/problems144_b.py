Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    for i in range(1, 10):
        for j in range(1, 10):
            if i * j == N:
                print("Yes")
                exit()
    print("No")

=======
Suggestion 2

def main():
    N = int(input())
    for i in range(1, 10):
        for j in range(1, 10):
            if i * j == N:
                print("Yes")
                return
    print("No")

=======
Suggestion 3

def main():
    n = int(input())
    for i in range(1, 10):
        for j in range(1, 10):
            if i * j == n:
                print("Yes")
                return
    print("No")

=======
Suggestion 4

def main():
    n = int(input())
    for i in range(1, 10):
        if n % i == 0 and n / i < 10:
            print("Yes")
            exit()
    print("No")

=======
Suggestion 5

def main():
    n = int(input())
    if n == 1 or n == 2 or n == 3 or n == 5 or n == 7:
        print('No')
    else:
        print('Yes')

=======
Suggestion 6

def main():
    n = int(input())
    for i in range(1, 10):
        if n % i == 0 and n / i < 10:
            print("Yes")
            return
    print("No")

=======
Suggestion 7

def main():
    n = int(input())
    for i in range(1,10):
        if n % i == 0:
            if n // i < 10:
                print("Yes")
                return
    print("No")

=======
Suggestion 8

def main():
    N = int(input())
    for i in range(1, 10):
        if N % i == 0 and N / i < 10:
            print("Yes")
            exit()
    print("No")
