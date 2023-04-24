Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    for i in range(1, 10):
        for j in range(1, 10):
            if i * j == n:
                print("Yes")
                return
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
    N = int(input())
    for i in range(1,10):
        for j in range(1,10):
            if i*j == N:
                print('Yes')
                return
    print('No')

=======
Suggestion 4

def main():
    n = int(input())
    for i in range(1,10):
        for j in range(1,10):
            if i*j == n:
                print('Yes')
                return
    print('No')

=======
Suggestion 5

def main():
    n = int(input())
    for i in range(1,10):
        for j in range(1,10):
            if i*j == n:
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

=======
Suggestion 7

def main():
    N = int(input())
    for i in range(1,10):
        if (N%i == 0) and (N//i < 10):
            print("Yes")
            return
    print("No")
