Synthesizing 8/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    x = list(map(int, input().split()))
    x_abs = list(map(abs, x))
    print(sum(x_abs))
    print(sum(map(lambda x: x**2, x_abs))**0.5)
    print(max(x_abs))

=======
Suggestion 2

def manhattanDistance(x):
    return sum(map(abs, x))

=======
Suggestion 3

def main():
    import math
    N = int(input())
    x = list(map(int, input().split()))
    print(sum([abs(x[i]) for i in range(N)]))
    print(sum([x[i]*x[i] for i in range(N)])**(1/2))
    print(max([abs(x[i]) for i in range(N)]))

=======
Suggestion 4

def main():
    n = int(input())
    x = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += abs(x[i])
    print(ans)
    ans = 0
    for i in range(n):
        ans += x[i]*x[i]
    print(ans**0.5)
    ans = 0
    for i in range(n):
        ans = max(ans, abs(x[i]))
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    x = [int(x) for x in input().split()]
    x_abs = [abs(x[i]) for i in range(n)]
    print(sum(x_abs))
    print(sum([x_abs[i]**2 for i in range(n)])**0.5)
    print(max(x_abs))

=======
Suggestion 6

def main():
    N = int(input())
    x = list(map(int,input().split()))
    print(sum([abs(i) for i in x]))
    print(sum([i**2 for i in x])**0.5)
    print(max([abs(i) for i in x]))
