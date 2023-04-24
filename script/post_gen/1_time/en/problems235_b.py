Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    H = list(map(int, input().split()))
    maxH = H[0]
    for i in range(1, N):
        if H[i] >= maxH:
            maxH = H[i]
    print(maxH)

=======
Suggestion 2

def main():
    n = int(input())
    h = list(map(int, input().split()))
    max_h = h[0]
    for i in range(1, n):
        if h[i] >= max_h:
            max_h = h[i]
    print(max_h)

=======
Suggestion 3

def main():
    N = int(input())
    H = list(map(int, input().split()))
    max_height = 0
    for i in range(N):
        if H[i] >= max_height:
            max_height = H[i]
    print(max_height)

=======
Suggestion 4

def main():
    n = int(input())
    h = list(map(int, input().split()))
    max_h = h[0]
    for i in range(n):
        if h[i] >= max_h:
            max_h = h[i]
    print(max_h)

=======
Suggestion 5

def main():
    N = int(input())
    H = list(map(int, input().split()))
    max = 0
    for i in range(N):
        if H[i] >= max:
            max = H[i]
    print(max)

=======
Suggestion 6

def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if ans < h[i]:
            ans = h[i]
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    H = [int(x) for x in input().split()]
    maxH = H[0]
    for i in range(1, N):
        if H[i] >= maxH:
            maxH = H[i]
    print(maxH)

=======
Suggestion 8

def main():
    N = int(input())
    H = [int(h) for h in input().split()]
    ans = H[0]
    for i in range(1, N):
        if H[i] >= ans:
            ans = H[i]
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        if H[i] >= H[i - 1]:
            ans = max(ans, H[i])
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    hi = list(map(int, input().split()))
    maxh = hi[0]
    for i in range(1,n):
        if hi[i] >= maxh:
            maxh = hi[i]
    print(maxh)
