Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    x = list(map(int, input().split()))
    print(sum(map(abs, x)))
    print(sum(map(lambda x: x**2, x))**0.5)
    print(max(map(abs, x)))

=======
Suggestion 2

def main():
    n = int(input())
    x = list(map(int,input().split()))
    sum = 0
    for i in range(n):
        sum += abs(x[i])
    print(sum)
    sum = 0
    for i in range(n):
        sum += x[i]*x[i]
    print(sum**0.5)
    max = 0
    for i in range(n):
        if max < abs(x[i]):
            max = abs(x[i])
    print(max)

=======
Suggestion 3

def main():
    n = int(input())
    x = list(map(int, input().split()))
    x_abs = [abs(i) for i in x]
    print(sum(x_abs))
    print(sum([i**2 for i in x_abs])**0.5)
    print(max(x_abs))

=======
Suggestion 4

def manhattan_distance(x):
    return sum([abs(i) for i in x])

=======
Suggestion 5

def manhattan_distance(x):
    return sum(map(abs, x))

=======
Suggestion 6

def main():
    n = int(input())
    x = list(map(int, input().split()))
    x_abs = list(map(abs, x))
    print(sum(x_abs))
    print(sum([i*i for i in x_abs])**0.5)
    print(max(x_abs))

=======
Suggestion 7

def main():
    N = int(input())
    x = list(map(int, input().split()))
    x_abs = [abs(i) for i in x]
    print(sum(x_abs))
    print(sum([i**2 for i in x_abs])**0.5)
    print(max(x_abs))

=======
Suggestion 8

def manhattan_dist(x):
    return sum([abs(i) for i in x])
