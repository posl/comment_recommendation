Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    flag = False
    for i in range(1, 10):
        for j in range(1, 10):
            if n == i * j:
                flag = True
                break
    if flag:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    n = int(input())
    for i in range(1, 10):
        for j in range(1, 10):
            if i * j == n:
                print("Yes")
                return
    print("No")

=======
Suggestion 3

def solution():
    N = int(input())
    for i in range(1, 10):
        if N % i == 0 and N / i < 10:
            print("Yes")
            break
    else:
        print("No")

=======
Suggestion 4

def main():
    n = int(input())
    for i in range(1, 10):
        for j in range(1, 10):
            if i * j == n:
                print("Yes")
                exit()
    print("No")

=======
Suggestion 5

def main():
    N = int(input())
    flag = False
    for i in range(1,10):
        if N % i == 0 and 1 <= N // i <= 9:
            flag = True
            break
    if flag:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    n = int(input())
    for i in range(1, 10):
        for j in range(1, 10):
            if n == i * j:
                print('Yes')
                return
    print('No')

=======
Suggestion 7

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

=======
Suggestion 8

def main():
    n = int(input())
    for i in range(1,10):
        if n % i == 0 and 1 <= n / i < 10:
            print("Yes")
            return
    print("No")

=======
Suggestion 9

def solve():
    n = int(input())
    for i in range(1, 10):
        for j in range(1, 10):
            if n == i * j:
                print("Yes")
                return
    print("No")

=======
Suggestion 10

def main():
    n = int(input())
    for i in range(1, 10):
        if n % i == 0 and n / i < 10:
            print("Yes")
            return
    print("No")
