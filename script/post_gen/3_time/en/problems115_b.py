Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    p = [int(input()) for _ in range(N)]
    p.sort()
    ans = 0
    for i in range(N-1):
        ans += p[i]
    ans += p[-1]//2
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    p = [int(input()) for i in range(N)]
    p.sort()
    ans = 0
    for i in range(N-1):
        ans += p[i]
    ans += p[N-1] // 2
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    p = []
    for i in range(N):
        p.append(int(input()))
    p.sort(reverse=True)
    total = 0
    for i in range(N):
        if i == 0:
            total += p[i] / 2
        else:
            total += p[i]
    print(int(total))

=======
Suggestion 4

def main():
    N = int(input())
    p = []
    for i in range(N):
        p.append(int(input()))
    p.sort(reverse=True)
    sum = 0
    for i in range(N):
        if i == 0:
            sum += p[i] // 2
        else:
            sum += p[i]
    print(sum)

=======
Suggestion 5

def main():
    n = int(input())
    p = [int(input()) for _ in range(n)]
    p.sort()
    ans = p[-1] // 2
    for i in range(n - 1):
        ans += p[i]
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    p = [int(input()) for _ in range(N)]
    p.sort(reverse=True)
    print(sum(p[1:]) + p[0] // 2)

=======
Suggestion 7

def main():
    N = int(input())
    P = [int(input()) for i in range(N)]

    P.sort()
    P[-1] = P[-1] // 2

    print(sum(P))

=======
Suggestion 8

def main():
    N = int(input())
    p = [int(input()) for _ in range(N)]
    p.sort()
    print(sum(p[:N-1]) + p[-1] // 2)

=======
Suggestion 9

def main():
    # Read input
    N = int(input())
    p = []
    for _ in range(N):
        p.append(int(input()))

    # Find the highest value
    max_value = max(p)

    # Find the total amount
    total = 0
    for i in range(N):
        if p[i] == max_value:
            total += p[i] / 2
        else:
            total += p[i]

    # Print the total amount
    print(int(total))
