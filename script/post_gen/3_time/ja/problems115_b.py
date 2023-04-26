Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    p.sort(reverse=True)
    p[0] = p[0] / 2
    print(int(sum(p)))

=======
Suggestion 2

def main():
    N = int(input())
    P = []
    for i in range(N):
        P.append(int(input()))
    P.sort()
    P[N-1] = int(P[N-1] / 2)
    print(sum(P))

=======
Suggestion 3

def solve():
    n = int(input())
    p = [int(input()) for _ in range(n)]
    p.sort(reverse=True)
    p[0] = p[0] // 2
    print(sum(p))

=======
Suggestion 4

def main():
    n = int(input())
    price = []
    for i in range(n):
        price.append(int(input()))
    price.sort()
    price[-1] = price[-1] // 2
    print(sum(price))

=======
Suggestion 5

def main():
    N = int(input())
    p_list = []
    for i in range(N):
        p_list.append(int(input()))

    p_list.sort()
    p_list[-1] /= 2

    print(int(sum(p_list)))

=======
Suggestion 6

def main():
    n = int(input())
    p = [int(input()) for _ in range(n)]
    max_p = max(p)
    p.remove(max_p)
    print(sum(p) + max_p // 2)

=======
Suggestion 7

def main():
    n = int(input())
    p = [int(input()) for i in range(n)]
    p.sort()
    print(sum(p[0:n-1]) + int(p[n-1]/2))

=======
Suggestion 8

def solve():
    N = int(input())
    p = [int(input()) for i in range(N)]
    p.sort()
    print(sum(p) - p[-1]//2)

=======
Suggestion 9

def main():
    N = int(input())
    p = list()
    for i in range(N):
        p.append(int(input()))
    p.sort()
    print(sum(p) - int(p[-1]/2))

=======
Suggestion 10

def calc_price(n, p):
    max_p = max(p)
    p.remove(max_p)
    return sum(p) + max_p / 2
