Synthesizing 10/10 solutions (Duplicates hidden)

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

=======
Suggestion 2

def main():
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))
    X = 0
    Y = 0
    for i in range(N):
        if V[i] - C[i] > 0:
            X += V[i] - C[i]
            Y += C[i]
    print(X - Y)

=======
Suggestion 3

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
    print(X - Y)

=======
Suggestion 4

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
Suggestion 5

def main():
    N = int(input())
    V = list(map(int,input().split()))
    C = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        if V[i] - C[i] > 0:
            ans += V[i] - C[i]
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    diff = [v[i] - c[i] for i in range(n)]
    ans = 0
    for i in range(n):
        if diff[i] > 0:
            ans += diff[i]
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    V = [int(x) for x in input().split()]
    C = [int(x) for x in input().split()]
    print(sum([max(V[i]-C[i],0) for i in range(N)]))
