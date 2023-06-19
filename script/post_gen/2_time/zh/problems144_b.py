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
    n = int(input())
    for i in range(1,10):
        if n % i == 0 and n // i < 10:
            print("Yes")
            return
    print("No")

=======
Suggestion 3

def main():
    N = int(input())
    for i in range(1, 10):
        if N % i == 0 and N // i < 10:
            print("Yes")
            exit()
    print("No")

=======
Suggestion 4

def get_input():
    N = int(input())
    return N

=======
Suggestion 5

def main():
    n = int(input())
    for i in range(1, 10):
        for j in range(1, 10):
            if i * j == n:
                print('Yes')
                return
    print('No')
main()

=======
Suggestion 6

def main():
    n = int(input())
    for i in range(1,10):
        if n % i == 0 and n // i <= 9:
            print("Yes")
            return
    print("No")

=======
Suggestion 7

def solve():
    N = int(input())
    for i in range(1, 10):
        if N % i == 0 and N / i < 10:
            print("Yes")
            return
    print("No")

solve()

=======
Suggestion 8

def func(n):
    for i in range(1,10):
        if n % i == 0 and n / i <= 9:
            return "Yes"
    return "No"

=======
Suggestion 9

def main():
    n = int(input())
    for i in range(1, 10):
        for j in range(1, 10):
            if n == i * j:
                print("Yes")
                return
    print("No")
