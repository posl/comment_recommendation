Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    for i in range(1, 1000):
        if int(i * 0.08) == a and int(i * 0.1) == b:
            print(i)
            return
    print(-1)

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    for i in range(1, 1000):
        if int(i * 0.08) == a and int(i * 0.1) == b:
            print(i)
            return
    print(-1)
    return

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    for i in range(1, 1001):
        if int(i * 0.08) == a and int(i * 0.1) == b:
            print(i)
            return
    print(-1)

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    for i in range(1, 10000):
        if int(i * 0.08) == a and int(i * 0.1) == b:
            print(i)
            exit()
    print(-1)

=======
Suggestion 5

def solve(a, b):
    for i in range(1, 10000):
        if int(i * 0.08) == a and int(i * 0.1) == b:
            return i
    return -1

=======
Suggestion 6

def solve(a, b):
    for i in range(1, 1001):
        if int(i * 0.08) == a and int(i * 0.1) == b:
            return i
    return -1

=======
Suggestion 7

def main():
    A, B = map(int, input().split())
    for i in range(1,1000):
        if int(i*0.08) == A and int(i*0.1) == B:
            print(i)
            exit()
    print(-1)

=======
Suggestion 8

def main():
    a,b = map(int, input().split())
    for i in range(1,1000):
        if (i*8)//100 == a and (i*10)//100 == b:
            print(i)
            return
    print(-1)

=======
Suggestion 9

def solution(a,b):
    for i in range(1,1001):
        if int(i*0.08) == a and int(i*0.1) == b:
            return i
    return -1

=======
Suggestion 10

def calc_tax(price, tax):
    return int(price * tax)
