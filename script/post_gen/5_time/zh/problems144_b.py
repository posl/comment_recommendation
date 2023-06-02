Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    flag = False
    for i in range(1, 10):
        if n % i == 0 and n / i < 10:
            flag = True
            break

    if flag:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    N = int(input())
    for i in range(1, 10):
        if N % i == 0 and N / i <= 9:
            print("Yes")
            return
    print("No")

=======
Suggestion 3

def problem144_b():
    n = int(input())
    for i in range(1, 10):
        for j in range(1, 10):
            if i * j == n:
                print('Yes')
                return
    print('No')

=======
Suggestion 4

def main():
    n = int(input())
    flag = False
    for i in range(1, 10):
        for j in range(1, 10):
            if i * j == n:
                flag = True
                break
    if flag:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    n = int(input())
    for i in range(1, 10):
        if n % i == 0 and n / i < 10:
            print("Yes")
            return
    print("No")

=======
Suggestion 6

def main():
    n = int(input())
    for i in range(1,10):
        if n % i == 0 and n / i < 10:
            print('Yes')
            exit()
    print('No')

=======
Suggestion 7

def main():
    n = int(input())
    for i in range(1,10):
        for j in range(1,10):
            if i*j == n:
                print("Yes")
                return
    print("No")

=======
Suggestion 8

def main():
    n = int(input())
    result = "No"
    for i in range(1,10):
        if n % i == 0 and n / i < 10:
            result = "Yes"
            break
    print(result)

=======
Suggestion 9

def solve():
    n = int(input())
    for i in range(1, 10):
        for j in range(1, 10):
            if i * j == n:
                print("Yes")
                return
    print("No")

solve()

=======
Suggestion 10

def main():
    n = int(input())
    for i in range(1, 10):
        if n % i == 0 and n // i < 10:
            print("Yes")
            exit()
    print("No")
