Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    p = []
    for i in range(N):
        p.append(int(input()))
    p.sort(reverse=True)
    ans = 0
    for i in range(N):
        if i == 0:
            ans += p[i] / 2
        else:
            ans += p[i]
    print(int(ans))

=======
Suggestion 2

def main():
    N = int(input())
    p = []
    for i in range(N):
        p.append(int(input()))
    p.sort(reverse=True)
    sum = 0
    for i in range(N):
        if i == 0:
            sum += p[i] / 2
        else:
            sum += p[i]
    print(int(sum))

=======
Suggestion 3

def main():
    N = int(input())
    p = []
    for _ in range(N):
        p.append(int(input()))
    p.sort(reverse=True)
    ans = p[0] / 2
    for i in range(1, N):
        ans += p[i]
    print(int(ans))

=======
Suggestion 4

def main():
    N = int(input())
    p = [int(input()) for i in range(N)]

    p.sort(reverse=True)
    ans = p[0] / 2
    for i in range(1, N):
        ans += p[i]

    print(int(ans))

=======
Suggestion 5

def main():
    N = int(input())
    p = []
    for i in range(N):
        p.append(int(input()))
    print(sum(p) - max(p) // 2)

=======
Suggestion 6

def main():
    N = int(input())
    p = [int(input()) for _ in range(N)]
    p.sort(reverse=True)
    print(int(p[0]/2 + sum(p[1:])))

=======
Suggestion 7

def main():
    n = int(input())
    p = [int(input()) for _ in range(n)]
    p.sort()
    print(sum(p) - p[-1]//2)

=======
Suggestion 8

def main():
    N = int(input())
    prices = [int(input()) for _ in range(N)]
    prices.sort()
    print(int((prices[-1] / 2) + sum(prices[:-1])))

=======
Suggestion 9

def main():
    N = int(input())
    p_list = []
    for i in range(N):
        p_list.append(int(input()))

    p_list.sort(reverse=True)
    #print(p_list)

    total = 0
    for i in range(N-1):
        total += p_list[i]

    total += p_list[-1] / 2
    print(total)

=======
Suggestion 10

def main():
    N = int(input())
    P = [int(input()) for _ in range(N)]

    max_p = max(P)
    P.remove(max_p)
    sum_p = sum(P)
    sum_p += max_p / 2

    print(sum_p)
