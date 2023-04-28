Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    p = []
    for i in range(N):
        p.append(int(input()))
    p.sort()
    p[-1] = p[-1] // 2
    print(sum(p))

=======
Suggestion 2

def main():
    n = int(input())
    p_list = []
    for i in range(n):
        p_list.append(int(input()))
    p_list.sort()
    p_list[n-1] = int(p_list[n-1]/2)
    print(sum(p_list))

=======
Suggestion 3

def main():
    n = int(input())
    p = [int(input()) for _ in range(n)]
    p.sort(reverse=True)
    p[0] = p[0] // 2
    print(sum(p))

=======
Suggestion 4

def main():
    N = int(input())
    p = [int(input()) for i in range(N)]
    p.sort(reverse=True)
    p[0] = p[0] / 2
    print(int(sum(p)))

=======
Suggestion 5

def main():
    N = int(input())
    p = []
    for i in range(N):
        p.append(int(input()))
    p.sort()
    p[-1] /= 2
    print(int(sum(p)))

=======
Suggestion 6

def main():
    N = int(input())
    p = []
    for i in range(0,N):
        p.append(int(input()))
    p.sort()
    p[N-1] = int(p[N-1] / 2)
    print(sum(p))

=======
Suggestion 7

def solve():
    N = int(input())
    p = [int(input()) for i in range(N)]
    p.sort(reverse=True)
    p[0] = p[0] / 2
    print(int(sum(p)))

=======
Suggestion 8

def main():
    # input
    N = int(input())
    P = [int(input()) for _ in range(N)]

    # compute
    P.sort()
    P[-1] //= 2
    ans = sum(P)

    # output
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    p = []
    for i in range(N):
        p.append(int(input()))
    p.sort()
    print(sum(p[0:-1]) + p[-1] // 2)

=======
Suggestion 10

def solve():
    N = int(input())
    p = [int(input()) for _ in range(N)]
    p.sort()
    print(sum(p[:-1]) + p[-1]//2)
