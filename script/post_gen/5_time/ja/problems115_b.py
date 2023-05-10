Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    p = [int(input()) for _ in range(n)]
    p.sort()
    print(sum(p[:-1]) + p[-1] // 2)

=======
Suggestion 2

def main():
    n = int(input())
    p = [int(input()) for i in range(n)]
    p.sort(reverse=True)
    p[0] = p[0] // 2
    print(sum(p))

=======
Suggestion 3

def main():
    n = int(input())
    p = [int(input()) for _ in range(n)]
    p.sort()
    print(sum(p) - int(p[-1] / 2))

=======
Suggestion 4

def problems115_b():
    N = int(input())
    p = []
    for i in range(N):
        p.append(int(input()))
    p.sort()
    p[N-1] = p[N-1]//2
    print(sum(p))

=======
Suggestion 5

def main():
    n = int(input())
    p = [int(input()) for _ in range(n)]
    p.sort(reverse=True)
    print(sum(p) - p[0]//2)

=======
Suggestion 6

def main():
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    p.sort(reverse=True)
    print(sum(p)-p[0]//2)

=======
Suggestion 7

def main():
    N = int(input())
    p = []
    for i in range(N):
        p.append(int(input()))
    p.sort()
    p[N-1] = p[N-1] // 2
    print(sum(p))

=======
Suggestion 8

def main():
    n = int(input())
    p = [int(input()) for _ in range(n)]
    p.sort(reverse=True)
    print(int(sum(p) - p[0]/2))

=======
Suggestion 9

def main():
    N = int(input())
    p = [int(input()) for _ in range(N)]
    p.sort(reverse=True)
    p[0] = p[0] // 2
    print(sum(p))

=======
Suggestion 10

def solve():
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    p.sort()
    p[-1] = p[-1] / 2
    print(int(sum(p)))
