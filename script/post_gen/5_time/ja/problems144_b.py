Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    for i in range(1,10):
        if n % i == 0 and n / i < 10:
            print("Yes")
            exit()
    print("No")

=======
Suggestion 2

def main():
    n = int(input())
    for i in range(1, 10):
        if n % i == 0 and n / i < 10:
            print('Yes')
            return
    print('No')

=======
Suggestion 3

def problem144_b():
    n = int(input())
    for i in range(1,10):
        if n % i == 0 and n / i <= 9:
            print('Yes')
            return
    print('No')

=======
Suggestion 4

def main():
    N = int(input())
    for i in range(1,10):
        for j in range(1,10):
            if N == i*j:
                print("Yes")
                return
    print("No")
main()

=======
Suggestion 5

def main():
    n = int(input())
    if n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def check(n):
    for i in range(1, 10):
        if n % i == 0 and n / i in range(1, 10):
            return True
    return False

n = int(input())
print('Yes' if check(n) else 'No')

=======
Suggestion 7

def Main():
    N = int(input())
    for i in range(1, 10):
        if N % i == 0 and N / i < 10:
            print('Yes')
            exit()
    print('No')

=======
Suggestion 8

def main():
    N = int(input())
    for i in range(1,10):
        if N % i == 0 and N / i <= 9:
            print("Yes")
            break
        elif i == 9:
            print("No")

=======
Suggestion 9

def main():
    N = int(input())
    for i in range(1, 10):
        if N % i == 0 and N / i <= 9:
            print('Yes')
            exit()
    print('No')

=======
Suggestion 10

def main():
    n = int(input())
    flag = False
    for i in range(1,10):
        if n % i == 0 and n//i < 10:
            flag = True
            break
    if flag:
        print('Yes')
    else:
        print('No')
