Synthesizing 8/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    x = list(map(int,input().split()))
    x = [abs(i) for i in x]
    print(sum(x))
    print(sum([i**2 for i in x])**0.5)
    print(max(x))

=======
Suggestion 2

def main():
    N = int(input())
    X = list(map(int,input().split()))
    manhattan_distance = 0
    euclidean_distance = 0
    chebyshev_distance = 0
    for i in range(N):
        manhattan_distance += abs(X[i])
        euclidean_distance += X[i]**2
        chebyshev_distance = max(chebyshev_distance,abs(X[i]))
    euclidean_distance = euclidean_distance**0.5
    print(manhattan_distance)
    print(euclidean_distance)
    print(chebyshev_distance)

=======
Suggestion 3

def manhattan_distance(x):
    return sum([abs(i) for i in x])

=======
Suggestion 4

def manhattan_distance(x):
    return sum(map(abs, x))

=======
Suggestion 5

def main():
    n = int(input())
    x = list(map(int, input().split()))
    for i in range(n):
        x[i] = abs(x[i])
    print(sum(x))
    print(sum([i ** 2 for i in x]) ** 0.5)
    print(max(x))

=======
Suggestion 6

def main():
    n = int(input())
    x = list(map(int, input().split()))
    x_abs = list(map(abs, x))
    print(sum(x_abs))
    print(sum(map(lambda x: x * x, x_abs)) ** 0.5)
    print(max(x_abs))

=======
Suggestion 7

def manhattan_distance(x):
    sum = 0
    for i in x:
        sum += abs(i)
    return sum
