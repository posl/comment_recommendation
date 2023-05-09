Synthesizing 7/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    x = list(map(int, input().split()))
    x = [abs(i) for i in x]
    print(sum(x))
    print(sum([i**2 for i in x])**0.5)
    print(max(x))

=======
Suggestion 2

def problem180_b():
    n = int(input())
    x = list(map(int, input().split()))
    x = [abs(i) for i in x]
    print(sum(x))
    print(sum([i**2 for i in x])**0.5)
    print(max(x))

=======
Suggestion 3

def distance(p):
    m = 0
    e = 0
    c = 0
    for i in p:
        m += abs(i)
        e += i**2
        if abs(i) > c:
            c = abs(i)
    e = e**0.5
    print(m)
    print(e)
    print(c)
    return

distance([-3, -1, -4, 1, -5, 9, 2, -6, 5, -3])

=======
Suggestion 4

def manhattan_distance(x, y):
    return sum(abs(x[i] - y[i]) for i in range(len(x)))

=======
Suggestion 5

def manhattan_distance(x):
    return sum([abs(i) for i in x])

=======
Suggestion 6

def manhattan_distance(x):
    return sum(abs(i) for i in x)
