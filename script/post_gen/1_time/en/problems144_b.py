Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    for i in range(1,10):
        for j in range(1,10):
            if N == i*j:
                print("Yes")
                return
    print("No")

=======
Suggestion 2

def main():
    n = int(input())
    for i in range(1,10):
        for j in range(1,10):
            if n == i * j:
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
    return

=======
Suggestion 4

def main():
    n = int(input())

    for i in range(1, 10):
        for j in range(1, 10):
            if i * j == n:
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
    N = int(input())
    
    for i in range(1, 10):
        for j in range(1, 10):
            if N == i * j:
                print("Yes")
                return
    print("No")
    return

=======
Suggestion 7

def main():
    n = int(input())
    for i in range(1,10):
        if n % i == 0 and n // i < 10:
            print("Yes")
            return
    print("No")

=======
Suggestion 8

def main():
    N = int(input())
    for i in range(1,10):
        if N % i == 0:
            if N // i < 10:
                print("Yes")
                return
    print("No")

=======
Suggestion 9

def main():
    N = int(input())

    if N == 1:
        print('No')
    else:
        for i in range(1, 10):
            if N % i == 0 and N // i <= 9:
                print('Yes')
                break
        else:
            print('No')

=======
Suggestion 10

def main():
    N = int(input())
    #print("N = ", N)
    for i in range(1, 10):
        for j in range(1, 10):
            #print("i = ", i, "j = ", j, "i*j = ", i*j)
            if i*j == N:
                print("Yes")
                return
    print("No")
    return
