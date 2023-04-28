Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    for i in range(1,10):
        for j in range(1,10):
            if n == i*j:
                print("Yes")
                exit()
    print("No")

=======
Suggestion 2

def main():
    n = int(input())
    for i in range(1, 10):
        if n % i == 0 and n / i <= 9:
            print('Yes')
            return
    print('No')

=======
Suggestion 3

def main():
    n = int(input())
    for i in range(1,10):
        if n % i == 0:
            if 1 <= n // i <= 9:
                print("Yes")
                exit()
    print("No")

=======
Suggestion 4

def main():
    N = int(input())
    for i in range(1,10):
        if N % i == 0 and N / i < 10:
            print("Yes")
            break
        elif i == 9:
            print("No")

=======
Suggestion 5

def main():
    n = int(input())
    for i in range(1, 10):
        if n % i == 0:
            if n / i <= 9:
                print("Yes")
                exit()
    print("No")

=======
Suggestion 6

def main():
    N = int(input())
    for x in range(1,10):
        for y in range(1,10):
            if N == x * y:
                print("Yes")
                return
    print("No")

=======
Suggestion 7

def main():
    n = int(input())
    for i in range(1,10):
        if n%i == 0 and n//i <= 9:
            print("Yes")
            return
    print("No")

=======
Suggestion 8

def main():
    n = int(input())
    for i in range(1,10):
        if n%i == 0 and n/i <= 9:
            print("Yes")
            exit()
    print("No")

=======
Suggestion 9

def solve(N):
    for i in range(1,10):
        if N % i == 0 and N / i < 10:
            return "Yes"
    return "No"

=======
Suggestion 10

def main():
    n = int(input())
    for i in range(1,10):
        if n%i==0 and n/i<10:
            print('Yes')
            return
    print('No')
    return
