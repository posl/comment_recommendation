Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    sum = 0
    for i in range(1, n+1):
        sum += i
        if sum >= n:
            print(i)
            break

=======
Suggestion 2

def main():
    n = int(input())
    sum = 0
    for i in range(1, 1000000):
        sum += i
        if sum >= n:
            print(i)
            break

=======
Suggestion 3

def main():
    n = int(input())
    sum = 0
    for i in range(1, n+1):
        sum += i
        if sum >= n:
            print(i)
            exit()

=======
Suggestion 4

def calc():
    N = int(input())
    sum = 0
    for i in range(1, N+1):
        sum += i
        if sum >= N:
            print(i)
            return
    print("error")

=======
Suggestion 5

def main():
    n = int(input())
    i = 1
    while True:
        if n <= i * (i + 1) / 2:
            break
        i += 1
    print(i)

=======
Suggestion 6

def main():
    N = int(input())
    sum = 0
    for i in range(1, 10**9+1):
        sum += i
        if sum >= N:
            print(i)
            break

=======
Suggestion 7

def solve():
    n = int(input())
    sum = 0
    for i in range(1, n + 1):
        sum += i
        if sum >= n:
            print(i)
            break
solve()

=======
Suggestion 8

def main():
    N = int(input())
    total = 0
    for i in range(1, N + 1):
        total += i
        if total >= N:
            print(i)
            break
