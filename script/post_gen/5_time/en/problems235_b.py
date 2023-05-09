Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    H = list(map(int, input().split()))
    maxH = 0
    for i in range(N):
        if H[i] >= maxH:
            maxH = H[i]
    print(maxH)

=======
Suggestion 2

def main():
    n = int(input())
    heights = list(map(int, input().split()))

    max_height = heights[0]
    for i in range(1, n):
        if heights[i] > max_height:
            max_height = heights[i]

    print(max_height)

=======
Suggestion 3

def main():
    N = int(input())
    H = list(map(int, input().split()))
    current_height = H[0]
    for i in range(1, N):
        if current_height < H[i]:
            current_height = H[i]
    print(current_height)

=======
Suggestion 4

def main():
    n = int(input())
    h = list(map(int, input().split()))
    i = 0
    while i < n - 1:
        if h[i] < h[i + 1]:
            h[i + 1] -= 1
            i = 0
        else:
            i += 1
    print(h[n - 1])

=======
Suggestion 5

def main():
    n = int(input())
    h = list(map(int, input().split()))
    max_h = 0
    count = 0
    for i in range(n - 1):
        if h[i] >= h[i + 1]:
            count += 1
            if count > max_h:
                max_h = count
        else:
            count = 0
    print(max_h)

=======
Suggestion 6

def main():
    n = int(input())
    h = [int(x) for x in input().split()]
    max_h = 0
    for i in range(n):
        if h[i] >= max_h:
            max_h = h[i]
    print(max_h)

=======
Suggestion 7

def solve():
    N = int(input())
    H = list(map(int, input().split()))
    max = H[0]
    for i in range(1, N):
        if H[i] >= max:
            max = H[i]
    print(max)

=======
Suggestion 8

def solve():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if i == 0:
            ans += h[i]
        elif h[i] > h[i-1]:
            ans += h[i] - h[i-1]
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    H = list(map(int,input().split()))

    maxH = 0
    for i in range(1,N):
        if H[i-1] < H[i]:
            H[i] = H[i-1]
        else:
            maxH = max(maxH,H[i-1])

    print(H[N-1] if maxH < H[N-1] else maxH)
