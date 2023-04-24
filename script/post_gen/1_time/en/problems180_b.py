Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    x = [int(i) for i in input().split()]
    manhattan = 0
    euclidian = 0
    chebyshev = 0
    for i in range(N):
        manhattan += abs(x[i])
        euclidian += abs(x[i]) ** 2
        if chebyshev < abs(x[i]):
            chebyshev = abs(x[i])
    euclidian = euclidian ** (1/2)
    print(manhattan)
    print(euclidian)
    print(chebyshev)

=======
Suggestion 2

def main():
    N = int(input())
    x = list(map(int, input().split()))
    print(sum(abs(i) for i in x))
    print((sum(i**2 for i in x))**0.5)
    print(max(abs(i) for i in x))

=======
Suggestion 3

def main():
    N = int(input())
    x = list(map(int, input().split()))
    print(sum(map(abs, x)))
    print((sum(map(lambda x: x**2, x)))**0.5)
    print(max(map(abs, x)))

=======
Suggestion 4

def main():
    N = int(input())
    x = list(map(int, input().split()))
    print(sum(map(abs, x)))
    print((sum(map(lambda i: i ** 2, x))) ** 0.5)
    print(max(map(abs, x)))

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(sum(abs(x) for x in a))
    print((sum(x*x for x in a))**0.5)
    print(max(abs(x) for x in a))

=======
Suggestion 6

def main():
    N = int(input())
    x = list(map(int, input().split()))
    print(sum([abs(xi) for xi in x]))
    print(pow(sum([xi**2 for xi in x]), 0.5))
    print(max([abs(xi) for xi in x]))

=======
Suggestion 7

def manhattan(x):
    return sum([abs(i) for i in x])

=======
Suggestion 8

def manhattan_distance(x):
    return sum([abs(x_i) for x_i in x])

=======
Suggestion 9

def manhattan_distance(x_list):
    return sum(abs(x) for x in x_list)

=======
Suggestion 10

def manhattan_distance(x):
    return sum(map(abs, x))
