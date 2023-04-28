Synthesizing 9/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    x = list(map(int, input().split()))
    print(sum(map(abs, x)))
    print(sum(map(lambda x: x**2, x))**0.5)
    print(max(map(abs, x)))

=======
Suggestion 2

def main():
    N = int(input())
    x = list(map(int, input().split()))
    res1 = 0
    res2 = 0
    res3 = 0
    for i in range(N):
        res1 += abs(x[i])
        res2 += x[i]**2
        res3 = max(res3, abs(x[i]))
    res2 = res2**0.5
    print(res1)
    print(res2)
    print(res3)

=======
Suggestion 3

def main():
    N = int(input())
    x = list(map(int, input().split()))
    x_abs = [abs(x[i]) for i in range(N)]
    print(sum(x_abs))
    print(sum([x_abs[i]**2 for i in range(N)])**(1/2))
    print(max(x_abs))

=======
Suggestion 4

def main():
    import sys
    import math

    # input
    N = int(input())
    x = list(map(int, input().split()))

    # compute
    ans = 0
    for i in range(N):
        ans += abs(x[i])
    print(ans)

    ans = 0
    for i in range(N):
        ans += x[i]**2
    ans = math.sqrt(ans)
    print(ans)

    ans = 0
    for i in range(N):
        if ans < abs(x[i]):
            ans = abs(x[i])
    print(ans)

=======
Suggestion 5

def manhattan_distance(x):
    return sum([abs(i) for i in x])
