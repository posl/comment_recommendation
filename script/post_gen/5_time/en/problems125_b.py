Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))
    X = 0
    Y = 0
    for i in range(N):
        if V[i] > C[i]:
            X += V[i]
            Y += C[i]
    print(X-Y)

=======
Suggestion 2

def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        if v[i] > c[i]:
            ans += v[i] - c[i]

    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    v = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    x = 0
    for i in range(n):
        if v[i] > c[i]:
            x += v[i] - c[i]
    print(x)

=======
Suggestion 4

def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    print(sum([max(0, v[i] - c[i]) for i in range(n)]))

=======
Suggestion 5

def solve():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        diff = v[i] - c[i]
        if diff > 0:
            ans += diff
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    x_y = [v[i] - c[i] for i in range(n)]
    print(sum([x_y[i] for i in range(n) if x_y[i] > 0]))

=======
Suggestion 7

def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))

    x_y = 0
    for i in range(n):
        if v[i] > c[i]:
            x_y += v[i] - c[i]
    print(x_y)

=======
Suggestion 8

def max_profit(N, V, C):
    profit = 0
    for i in range(N):
        if V[i] > C[i]:
            profit += V[i] - C[i]
    return profit

N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))
print(max_profit(N, V, C))

=======
Suggestion 9

def main():
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))

    print(sum([max(0, v-c) for v, c in zip(V, C)]))

=======
Suggestion 10

def max_value(n,v,c):
    v.sort(reverse=True)
    c.sort(reverse=True)
    return sum([v[i]-c[i] for i in range(n) if v[i]>c[i]])
