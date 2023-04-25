Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    x = list(map(int, input().split()))
    m = 0
    e = 0
    c = 0
    for i in range(n):
        m += abs(x[i])
        e += x[i] ** 2
        if abs(x[i]) > c:
            c = abs(x[i])
    e = e ** 0.5
    print(m)
    print(e)
    print(c)

=======
Suggestion 2

def main():
    N = int(input())
    X = list(map(int, input().split()))
    print(sum([abs(x) for x in X]))
    print((sum([x**2 for x in X]))**0.5)
    print(max([abs(x) for x in X]))

=======
Suggestion 3

def main():
    N = int(input())
    X = [int(x) for x in input().split()]
    print(sum(abs(x) for x in X))
    print((sum(x**2 for x in X))**0.5)
    print(max(abs(x) for x in X))
main()

=======
Suggestion 4

def main():
    N = int(input())
    x = list(map(int,input().split()))
    print(sum([abs(i) for i in x]))
    print((sum([i**2 for i in x]))**(1/2))
    print(max([abs(i) for i in x]))

=======
Suggestion 5

def main():
    n = int(input())
    x = list(map(int, input().split()))
    print(sum([abs(i) for i in x]))
    print(sum([i ** 2 for i in x]) ** 0.5)
    print(max([abs(i) for i in x]))

=======
Suggestion 6

def main():
    N = int(input())
    x = list(map(int, input().split()))
    print(sum([abs(x[i]) for i in range(N)]))
    print((sum([x[i]**2 for i in range(N)]))**0.5)
    print(max([abs(x[i]) for i in range(N)]))

=======
Suggestion 7

def main():
    N = int(input())
    x = list(map(int, input().split()))
    print(sum([abs(i) for i in x]))
    print((sum([i*i for i in x]))**0.5)
    print(max([abs(i) for i in x]))

=======
Suggestion 8

def main():
    N = int(input())
    x = list(map(int, input().split()))

    # Manhattan distance
    print(sum(map(abs, x)))

    # Euclidian distance
    print((sum(map(lambda x: x**2, x)))**0.5)

    # Chebyshev distance
    print(max(map(abs, x)))

=======
Suggestion 9

def manhattan_distance(x):
    return sum([abs(i) for i in x])

=======
Suggestion 10

def read_ints():
    return list(map(int, input().split()))
