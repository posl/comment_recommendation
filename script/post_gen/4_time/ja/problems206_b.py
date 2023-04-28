Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    sum = 0
    i = 0
    while True:
        i += 1
        sum += i
        if sum >= n:
            break
    print(i)

=======
Suggestion 2

def main():
    n = int(input())
    sum = 0
    for i in range(1, n):
        sum += i
        if sum >= n:
            print(i)
            break

=======
Suggestion 3

def main():
    n = int(input())
    sum = 0
    i = 0
    while sum < n:
        i += 1
        sum += i
    print(i)

=======
Suggestion 4

def main():
    # input
    N = int(input())

    # compute
    sum = 0
    for i in range(1, N+1):
        sum += i
        if sum >= N:
            break

    # output
    print(i)

=======
Suggestion 5

def calc(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
        if sum >= n:
            return i

n = int(input())
print(calc(n))

=======
Suggestion 6

def main():
    # input
    N = int(input())

    # compute
    i = 1
    while True:
        if N <= i*(i+1)/2:
            break
        i += 1

    # output
    print(i)

=======
Suggestion 7

def main():
    N = int(input())
    day = 0
    for i in range(1, N+1):
        day += i
        if day >= N:
            print(i)
            break

=======
Suggestion 8

def main():
    N = int(input())
    i = 1
    while True:
        if (i * (i + 1) / 2) >= N:
            print(i)
            break
        i += 1

=======
Suggestion 9

def main():
    N = int(input())
    i = 1
    while True:
        if N <= i*(i+1)/2:
            print(i)
            break
        i += 1

=======
Suggestion 10

def main():

    N = int(input())

    sum = 0
    for i in range(1, 1000000):
        sum += i
        if sum >= N:
            print(i)
            break
