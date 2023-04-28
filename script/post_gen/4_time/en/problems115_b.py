Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    p = []
    for i in range(N):
        p.append(int(input()))
    p.sort()
    sum = 0
    for i in range(N-1):
        sum += p[i]
    sum += p[N-1]/2
    print(int(sum))

=======
Suggestion 2

def main():
    n = int(input())
    p = [int(input()) for _ in range(n)]
    p.sort()
    ans = 0
    for i in range(n-1):
        ans += p[i]
    ans += p[-1] // 2
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    p = [int(input()) for i in range(N)]
    p.sort(reverse=True)
    ans = 0
    for i in range(N):
        if i == 0:
            ans += p[i] // 2
        else:
            ans += p[i]
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    p = []
    for _ in range(n):
        p.append(int(input()))
    p.sort(reverse=True)
    sum = 0
    for i in range(1, n):
        sum += p[i]
    sum += p[0] // 2
    print(sum)

=======
Suggestion 5

def main():
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    p.sort()
    p.reverse()
    ans = 0
    for i in range(n):
        if i % 2 == 0:
            ans += p[i]
        else:
            ans += p[i] / 2
    print(int(ans))

=======
Suggestion 6

def main():
    N = int(input())
    prices = [int(input()) for i in range(N)]
    prices.sort()
    prices[-1] = int(prices[-1] / 2)
    print(sum(prices))

=======
Suggestion 7

def main():
    N = int(input())
    p = [int(input()) for _ in range(N)]
    p.sort(reverse=True)
    print(sum(p[1:]) + p[0] // 2)

=======
Suggestion 8

def main():
    n = int(input())
    p = [int(input()) for _ in range(n)]
    p.sort()
    print(sum(p[:-1]) + p[-1]//2)

main()

=======
Suggestion 9

def main():
    N = int(input())
    p = [int(input()) for i in range(N)]
    p.sort()
    print(sum(p[:-1]) + p[-1] // 2)

=======
Suggestion 10

def main():
    #write your code below this line
    pass
