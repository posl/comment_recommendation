Synthesizing 8/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    x = list(map(int, input().split()))

    a = 0
    b = 0
    c = 0

    for i in range(n):
        a += abs(x[i])
        b += x[i]**2
        c = max(c, abs(x[i]))

    print(a)
    print(b**(1/2))
    print(c)

=======
Suggestion 2

def main():
    n = int(input())
    x = list(map(int, input().split()))
    x = [abs(i) for i in x]
    print(sum(x))
    print(sum([i ** 2 for i in x]) ** 0.5)
    print(max(x))

=======
Suggestion 3

def main():
    N = int(input())
    x = list(map(int, input().split()))
    x = [abs(x) for x in x]
    print(sum(x))
    print(sum([i ** 2 for i in x]) ** 0.5)
    print(max(x))

=======
Suggestion 4

def manhattan_distance(x):
    return sum(abs(i) for i in x)

=======
Suggestion 5

def manhattan_distance(x):
    return sum(abs(xi) for xi in x)

=======
Suggestion 6

def manhattan_distance(x):
    return sum(map(abs, x))

=======
Suggestion 7

def distance(x):
    return sum(map(lambda x: abs(x), x))

=======
Suggestion 8

def ManhattanDistance(x):
    return sum(map(abs, x))
