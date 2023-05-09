Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 1
    max = H[0]
    for i in range(1, N):
        if max <= H[i]:
            count += 1
            max = H[i]
    print(count)

=======
Suggestion 2

def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    max = 0
    for i in range(n):
        if max <= h[i]:
            count += 1
            max = h[i]
    print(count)

=======
Suggestion 3

def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    max = 0
    for i in range(n):
        if max <= h[i]:
            max = h[i]
            count += 1
    print(count)

=======
Suggestion 4

def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 1
    for i in range(1, n):
        if h[i] >= max(h[:i]):
            count += 1
    print(count)

=======
Suggestion 5

def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    max_height = 0
    for i in range(n):
        if h[i] >= max_height:
            max_height = h[i]
            count += 1
    print(count)

=======
Suggestion 6

def main():
    n = int(input())
    heights = list(map(int, input().split()))
    count = 1
    max_height = heights[0]
    for i in range(1, n):
        if heights[i] >= max_height:
            count += 1
            max_height = heights[i]
    print(count)

=======
Suggestion 7

def solve():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 1
    for i in range(1, n):
        if max(h[:i]) <= h[i]:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    h_list = list(map(int, input().split()))
    count = 1
    max_h = h_list[0]
    for i in range(1, n):
        if max_h <= h_list[i]:
            count += 1
            max_h = h_list[i]
    print(count)
    return

=======
Suggestion 9

def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if i == 0:
            count += 1
        elif max(h[:i]) <= h[i]:
            count += 1
    print(count)

=======
Suggestion 10

def main():
    #input
    n = int(input())
    h = list(map(int, input().split()))

    #compute
    count = 1
    for i in range(1, n):
        for j in range(0, i):
            if h[j] > h[i]:
                break
        else:
            count += 1

    #output
    print(count)
