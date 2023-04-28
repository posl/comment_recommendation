Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 1
    for i in range(1, N):
        if H[i-1] <= H[i]:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    n = int(input())
    h = list(map(int, input().split()))
    cnt = 1
    for i in range(1, n):
        if max(h[:i]) <= h[i]:
            cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    max = 0
    for i in range(n):
        if h[i] >= max:
            count += 1
            max = h[i]
    print(count)

=======
Suggestion 4

def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 0
    for i in range(1, N):
        if max(H[:i]) <= H[i]:
            count += 1
    print(count + 1)

=======
Suggestion 5

def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 1
    for i in range(1, n):
        if h[i] >= max(h[0:i]):
            count += 1
    print(count)

=======
Suggestion 6

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
Suggestion 7

def main():
    n = int(input())
    h_list = list(map(int, input().split()))
    count = 0
    max_height = 0
    for h in h_list:
        if h >= max_height:
            count += 1
            max_height = h
    print(count)

=======
Suggestion 8

def main():
    N = int(input())
    H = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if i == 0:
            cnt += 1
        elif H[i-1] <= H[i]:
            cnt += 1
    print(cnt)

=======
Suggestion 9

def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if i == 0:
            count += 1
        elif i > 0:
            if h[i] >= max(h[:i]):
                count += 1
    print(count)

=======
Suggestion 10

def main():
    N = int(input())
    H = list(map(int, input().split()))

    max = 0
    count = 0

    for i in range(0, N):
        if max <= H[i]:
            count += 1
            max = H[i]

    print(count)
