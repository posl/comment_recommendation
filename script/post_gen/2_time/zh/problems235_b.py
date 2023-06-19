Synthesizing 10/10 solutions

=======
Suggestion 1

def solution1():
    N = int(input())
    H = list(map(int, input().split()))
    max = 0
    for i in range(N):
        if H[i] >= max:
            max = H[i]
    print(max)

=======
Suggestion 2

def main():
    n = int(input())
    h = list(map(int, input().split()))
    max_h = 0
    for i in range(n):
        if h[i] >= max_h:
            max_h = h[i]
    print(max_h)

=======
Suggestion 3

def main():
    n = int(input())
    h = list(map(int, input().split()))
    current_h = h[0]
    for i in range(1, n):
        if h[i] > current_h:
            current_h = h[i]
    print(current_h)

=======
Suggestion 4

def main():
    N = int(input())
    H = list(map(int, input().split()))
    max_h = 0
    count = 0
    for i in range(N-1):
        if H[i] < H[i+1]:
            count += 1
        else:
            count = 0
        if count > max_h:
            max_h = count
    print(max_h+1)

=======
Suggestion 5

def solution():
    n = int(input())
    h = list(map(int, input().split()))
    last = h[0]
    for i in range(1, n):
        if h[i] > last:
            last = h[i]
    print(last)

solution()

=======
Suggestion 6

def main():
    n = int(input())
    h = list(map(int, input().split()))
    last = h[0]
    for i in range(1, n):
        if last < h[i]:
            last = h[i]
    print(last)

=======
Suggestion 7

def main():
    N = int(input())
    H = list(map(int, input().split()))
    max_h = 0
    for i in range(N):
        if H[i] >= max_h:
            max_h = H[i]
    print(max_h)

=======
Suggestion 8

def main():
    n = int(input())
    h = list(map(int, input().split()))
    max_h = 0
    for i in range(n):
        if max_h <= h[i]:
            max_h = h[i]
    print(max_h)

=======
Suggestion 9

def main():
    n = int(input())
    h = list(map(int, input().split()))
    maxH = 0
    for i in range(n):
        if h[i] >= maxH:
            maxH = h[i]
    print(maxH)

=======
Suggestion 10

def get_input():
    n = int(input())
    h = [int(i) for i in input().split()]
    return n, h
