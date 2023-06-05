Synthesizing 6/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    x = list(map(int, input().split()))
    x = [abs(x[i]) for i in range(n)]
    print(sum(x))
    print(sum([x[i]*x[i] for i in range(n)])**0.5)
    print(max(x))

=======
Suggestion 2

def main():
    n = int(input())
    x = list(map(int, input().split()))
    x_abs = list(map(abs, x))
    print(sum(x_abs))
    print(sum([x**2 for x in x_abs])**0.5)
    print(max(x_abs))

=======
Suggestion 3

def main():
    N = int(input())
    x = list(map(int, input().split()))
    x_abs = [abs(x[i]) for i in range(N)]
    print(sum(x_abs))
    print(sum(map(lambda x:x*x, x_abs))**0.5)
    print(max(x_abs))

=======
Suggestion 4

def main():
    n = int(input())
    x = list(map(int, input().split()))
    print(sum(map(abs, x)))
    print(sum(map(lambda x: x**2, x))**0.5)
    print(max(map(abs, x)))

=======
Suggestion 5

def manhattan_distance(N, x):
    return sum([abs(i) for i in x])

=======
Suggestion 6

def main():
    n = int(input())
    x = list(map(int, input().split()))
    x_abs = list(map(abs, x))
    print(sum(x_abs))
    print(sum(i**2 for i in x_abs)**(1/2))
    print(max(x_abs))
