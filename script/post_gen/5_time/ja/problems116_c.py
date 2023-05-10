Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    h = [int(x) for x in input().split()]
    ans = 0
    while True:
        if max(h) == 0:
            break
        else:
            l = 0
            r = 0
            for i in range(N):
                if h[i] > 0:
                    l = i
                    break
            for i in range(l,N):
                if h[i] == 0:
                    r = i
                    break
                elif i == N-1:
                    r = N
            for i in range(l,r):
                h[i] -= 1
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(1, n):
        if h[i] > h[i - 1]:
            ans += h[i] - h[i - 1]
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    h = list(map(int, input().split()))
    h.insert(0, 0)
    count = 0
    for i in range(1, n+1):
        if h[i] < h[i-1]:
            count += h[i-1] - h[i]
    print(count)

=======
Suggestion 4

def main():
    N = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(N-1):
        if h[i] < h[i+1]:
            ans += h[i+1] - h[i]
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(N-1):
        if h[i] > h[i+1]:
            ans += h[i] - h[i+1]
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if i == 0:
            ans += h[i]
        else:
            ans += max(h[i] - h[i-1], 0)
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if i == 0:
            ans += h[i]
        else:
            if h[i] > h[i-1]:
                ans += h[i] - h[i-1]

    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if i == 0:
            ans += h[i]
        elif h[i-1] < h[i]:
            ans += h[i] - h[i-1]
    print(ans)

=======
Suggestion 9

def solve():
    N = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(N-1):
        if h[i] < h[i+1]:
            ans += h[i+1] - h[i]
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if i == 0:
            ans += h[i]
        else:
            ans += abs(h[i] - h[i-1])
    print(ans)
