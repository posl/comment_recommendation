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
        for j in range(1,10):
            if i*j == n:
                print("Yes")
                return
    print("No")

=======
Suggestion 3

def main():
    n = int(input())
    for i in range(1,10):
        for j in range(1,10):
            if i*j == n:
                print("Yes")
                return
    print("No")
    return

main()

=======
Suggestion 4

def main():
    N = int(input())
    for i in range(1,10):
        for j in range(1,10):
            if i*j == N:
                print("Yes")
                return
    print("No")
    return

=======
Suggestion 5

def main():
    N = int(input())
    for i in range(1,10):
        for j in range(1,10):
            if N == i*j:
                print("Yes")
                return
    print("No")
    return

=======
Suggestion 6

def main():
    N = int(input())
    for i in range(1,10):
        if N % i == 0 and N // i < 10:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 7

def main():
    n = int(input())
    if n <= 9:
        print('No')
    else:
        for i in range(1, 10):
            if n % i == 0 and 1 <= n // i <= 9:
                print('Yes')
                break
        else:
            print('No')

=======
Suggestion 8

def is_multiple(x, y):
    return x * y

n = int(input())

for i in range(1, 10):
    for j in range(1, 10):
        if is_multiple(i, j) == n:
            print('Yes')
            exit()
print('No')
