Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    for i in range(1, 10):
        if N % i == 0 and N / i < 10:
            print("Yes")
            return
    print("No")

=======
Suggestion 2

def main():
    n = int(input())
    for i in range(1, 10):
        for j in range(1, 10):
            if n == i * j:
                print("Yes")
                return
    print("No")

=======
Suggestion 3

def main():
    n = int(input())
    for i in range(1,10):
        for j in range(1,10):
            if i * j == n:
                print("Yes")
                return
    print("No")

=======
Suggestion 4

def main():
    N = int(input())
    for i in range(1, 10):
        if N % i == 0 and 1 <= N / i <= 9:
            print("Yes")
            exit()
    print("No")

=======
Suggestion 5

def get_input():
    n = int(input())
    return n

=======
Suggestion 6

def main():
    N = int(input())
    for i in range(1, 10):
        if N % i == 0:
            if N / i <= 9:
                print("Yes")
                return
    print("No")

=======
Suggestion 7

def check(n):
    for i in range(1,10):
        for j in range(1,10):
            if i * j == n:
                return True
    return False

=======
Suggestion 8

def main():
    n = int(input())
    for i in range(1,10):
        if n % i == 0:
            if n / i <= 9:
                print("Yes")
                return
    print("No")

=======
Suggestion 9

def main():
    N = int(input())
    for i in range(1,10):
        if N%i == 0 and N/i <= 9:
            print("Yes")
            break
    else:
        print("No")

=======
Suggestion 10

def main():
    N = int(input())
    for i in range(1,10):
        if N % i == 0:
            if N / i < 10:
                print("Yes")
                return
    print("No")
