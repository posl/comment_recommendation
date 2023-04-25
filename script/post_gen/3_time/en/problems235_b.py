Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    H = list(map(int, input().split()))
    for i in range(N-1):
        if H[i] < H[i+1]:
            H[i] = H[i+1]
    print(H[-1])

=======
Suggestion 2

def main():
    n = int(input())
    h = list(map(int, input().split()))
    max_h = 0
    count = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            count += 1
        else:
            count = 0
        if count > max_h:
            max_h = count
    print(max_h+1)

=======
Suggestion 3

def main():
    N = int(input())
    H = list(map(int, input().split()))
    max_h = 0
    count = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
            count += 1
        else:
            count = 0
        if count > max_h:
            max_h = count
    print(max_h+1)

=======
Suggestion 4

def readinput():
    n=int(input())
    h=list(map(int,input().split()))
    return n,h

=======
Suggestion 5

def main():
    n = int(input())
    h = list(map(int, input().split()))
    max = 0
    count = 0
    for i in range(n-1):
        if h[i] < h[i+1]:
            count = 0
        else:
            count += 1
        if count > max:
            max = count
    print(h[max])

=======
Suggestion 6

def main():
    n = int(input())
    h = [int(x) for x in input().split()]
    max_h = h[0]
    for i in range(1, n):
        if h[i] >= max_h:
            max_h = h[i]
    print(max_h)

=======
Suggestion 7

def main():
    N = int(input())
    H = [int(x) for x in input().split()]
    maxH = 0
    for i in range(N):
        if H[i] >= maxH:
            maxH = H[i]
    print(maxH)

=======
Suggestion 8

def main():
    N = int(input())
    H = list(map(int, input().split()))
    maxH = 0
    count = 0
    for h in H:
        if h >= maxH:
            count += 1
            maxH = h
    print(maxH)

=======
Suggestion 9

def main():
    N = int(input())
    H = list(map(int, input().split()))

    ans = 0
    max_h = 0

    for i in range(N):
        if max_h <= H[i]:
            ans += 1
            max_h = H[i]

    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    h = list(map(int, input().split()))
    h.reverse()
    max_height = h[0]
    for i in range(1,n):
        if h[i] >= max_height:
            max_height = h[i]
    print(max_height)
