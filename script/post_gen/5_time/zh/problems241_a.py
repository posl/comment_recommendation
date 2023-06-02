Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a = map(int, raw_input().split())
    for i in range(3):
        a = a[a[0]]
    print a

=======
Suggestion 2

def a():
    pass

=======
Suggestion 3

def problem241_a():
    a = input().split()
    for i in range(3):
        a = a[int(a[0])]
    print(a)

=======
Suggestion 4

def main():
    a = [int(i) for i in input().split()]
    n = 0
    for i in range(3):
        n = a[n]
    print(n)

=======
Suggestion 5

def main():
    a = [int(x) for x in input().split()]
    n = len(a)
    for i in range(1, n):
        a[i] = a[a[i]]
    print(a[3])

=======
Suggestion 6

def main():
    a = [int(x) for x in input().split()]
    x = 0
    for i in range(3):
        x = a[x]
    print(x)

=======
Suggestion 7

def main():
    a = input().split()
    k = 0
    for i in range(3):
        k = int(a[k])
    print(k)

=======
Suggestion 8

def solve():
    a = map(int, raw_input().split())
    k = 0
    for i in range(3):
        k = a[k]
    print k

=======
Suggestion 9

def problems241_a():
    a = [int(i) for i in input().split()]
    k = 0
    for i in range(3):
        k = a[k]
    print(k)

=======
Suggestion 10

def func(a):
    for i in range(10):
        if a[i] == 0:
            return i
