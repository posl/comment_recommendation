Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    max_h = 0
    for i in range(n):
        if max_h <= h[i]:
            count += 1
            max_h = h[i]
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
            max = h[i]
            count += 1

    print(count)

=======
Suggestion 3

def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    max = 0
    for i in range(n):
        if h[i] >= max:
            ans += 1
            max = h[i]
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    h_list = list(map(int, input().split()))
    count = 0
    max_height = 0
    for h in h_list:
        if max_height <= h:
            max_height = h
            count += 1
    print(count)

=======
Suggestion 5

def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if i == 0:
            count += 1
        elif H[i-1] <= H[i]:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    N = int(input())
    H = list(map(int, input().split()))
    max = 0
    count = 0
    for i in range(N):
        if max <= H[i]:
            max = H[i]
            count += 1
    print(count)

=======
Suggestion 7

def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 1
    for i in range(1, n):
        if h[i] >= max(h[:i]):
            count += 1
    print(count)

=======
Suggestion 8

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
Suggestion 9

def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 1
    for i in range(1, N):
        if max(H[0:i]) <= H[i]:
            count += 1
    print(count)

=======
Suggestion 10

def main():
    n = int(input())
    h = list(map(int, input().split()))
    cnt = 1
    max_h = h[0]
    for i in range(1, n):
        if h[i] >= max_h:
            cnt += 1
            max_h = h[i]
    print(cnt)
