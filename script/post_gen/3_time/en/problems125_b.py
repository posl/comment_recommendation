Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if V[i] > C[i]:
            ans += V[i] - C[i]
    print(ans)

main()

=======
Suggestion 2

def main():
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if V[i] - C[i] > 0:
            ans += V[i] - C[i]
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if v[i] - c[i] > 0:
            ans += v[i] - c[i]
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    V = [int(x) for x in input().split()]
    C = [int(x) for x in input().split()]
    X = 0
    Y = 0
    for i in range(N):
        if V[i] > C[i]:
            X += V[i]
            Y += C[i]
    print(X-Y)

=======
Suggestion 5

def main():
    N = int(input())
    V = [int(v) for v in input().split()]
    C = [int(c) for c in input().split()]
    ans = 0
    for i in range(N):
        ans += max(0, V[i] - C[i])
    print(ans)

=======
Suggestion 6

def solve():
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if V[i] > C[i]:
            ans += V[i] - C[i]
    print(ans)

solve()

=======
Suggestion 7

def main():
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))
    X = 0
    for i in range(N):
        if V[i] > C[i]:
            X += V[i] - C[i]
    print(X)

=======
Suggestion 8

def main():
    # input
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))

    # compute
    ans = 0
    for i in range(N):
        if V[i] > C[i]:
            ans += V[i] - C[i]

    # output
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    values = list(map(int, input().split()))
    costs = list(map(int, input().split()))
    max_value = 0
    for i in range(N):
        if values[i] > costs[i]:
            max_value += values[i] - costs[i]
    print(max_value)

=======
Suggestion 10

def read_int():
    return int(input())
