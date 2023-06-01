Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    x = 0
    while x < n:
        x = x + 1
        if x * (x + 1) / 2 >= n:
            break
    print(x)

=======
Suggestion 2

def main():
    n = int(input())
    sum = 0
    for i in range(1, 100000):
        sum += i
        if sum >= n:
            print(i)
            break

=======
Suggestion 3

def f(n):
    return n*(n+1)/2

=======
Suggestion 4

def solve(n):
    sum = 0
    day = 1
    while sum < n:
        sum += day
        day += 1
    return day - 1

=======
Suggestion 5

def solve(n):
    s = 0
    for i in range(1, n+1):
        s += i
        if s >= n:
            return i
    return 0

=======
Suggestion 6

def problems206_b():
    n = int(input())
    x = 0
    for i in range(1, n+1):
        x += i
        if x >= n:
            print(i)
            return

=======
Suggestion 7

def main():
    n = int(input())
    x = 0
    while True:
        x += 1
        if x*(x+1)/2 >= n:
            break
    print(x)

=======
Suggestion 8

def sum(n):
    return int(n*(n+1)/2)

N = int(input())
x = 0
while sum(x) < N:
    x += 1
print(x)

=======
Suggestion 9

def main():
    n = int(input())
    sum = 0
    for i in range(1, n+1):
        sum += i
        if sum >= n:
            print(i)
            break

=======
Suggestion 10

def check(n):
    x = 0
    for i in range(1, n+1):
        x += i
        if x >= n:
            return i
