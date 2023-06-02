Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    x = [int(x) for x in input().split()]
    print(sum([abs(x[i]) for i in range(n)]))
    print(sum([x[i]**2 for i in range(n)])**0.5)
    print(max([abs(x[i]) for i in range(n)]))

=======
Suggestion 2

def manhattan_distance(x):
    return sum([abs(i) for i in x])

=======
Suggestion 3

def minkowski(x, y, p):
    return sum([abs(xi - yi) ** p for xi, yi in zip(x, y)]) ** (1 / p)

=======
Suggestion 4

def manhattan_distance(x):
    sum = 0
    for i in range(len(x)):
        sum += abs(x[i])
    return sum

=======
Suggestion 5

def main():
    N = int(input())
    x = input().split()
    x = [int(i) for i in x]
    x_manhattan = 0
    x_euclidean = 0
    x_chebyshev = 0
    for i in x:
        x_manhattan += abs(i)
        x_euclidean += i**2
        if abs(i) > x_chebyshev:
            x_chebyshev = abs(i)
    x_euclidean = x_euclidean**0.5
    print(x_manhattan)
    print(x_euclidean)
    print(x_chebyshev)

=======
Suggestion 6

def main():
    N = int(input())
    x = list(map(int, input().split()))
    print(sum(map(abs, x)))
    print(sum(map(lambda x: x**2, x))**0.5)
    print(max(map(abs, x)))

=======
Suggestion 7

def manhattan_distance(x):
    return sum(map(abs,x))

=======
Suggestion 8

def main():
    N = int(input())
    x = list(map(int,input().split()))
    #曼哈顿距离
    print(sum(map(abs,x)))
    #欧氏距离
    print(sum(map(lambda x:x**2,x))**0.5)
    #切比雪夫距离
    print(max(map(abs,x)))

=======
Suggestion 9

def main():
    n = int(input())
    x = list(map(int, input().split()))
    print(sum([abs(x[i]) for i in range(n)]))
    print(sum([x[i] ** 2 for i in range(n)]) ** 0.5)
    print(max([abs(x[i]) for i in range(n)]))

=======
Suggestion 10

def manhattan(x):
    return sum([abs(i) for i in x])
