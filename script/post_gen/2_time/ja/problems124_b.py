Synthesizing 10/10 solutions (Duplicates hidden)

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
    N = int(input())
    H = list(map(int, input().split()))
    ans = 1
    for i in range(1, N):
        if H[i-1] <= H[i]:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 1
    for i in range(1, n):
        if h[i-1] <= h[i]:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    H = list(map(int, input().split()))
    cnt = 1
    for i in range(N-1):
        if H[i] <= H[i+1]:
            cnt += 1
    print(cnt)

=======
Suggestion 5

def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 1
    for i in range(1, n):
        if h[i - 1] <= h[i]:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if i == 0:
            ans += 1
        else:
            if H[i-1] <= H[i]:
                ans += 1

    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    H = list(map(int, input().split()))

    ans = 1
    for i in range(1, N):
        if H[i-1] < H[i]:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if H[i] >= max(H[:i+1]):
            ans += 1
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    H = list(map(int, input().split()))
    if N == 1:
        print(1)
    else:
        count = 0
        for i in range(N):
            if i == 0:
                if H[i] <= H[i+1]:
                    count += 1
            elif i == N-1:
                if H[i] <= H[i-1]:
                    count += 1
            else:
                if H[i] <= H[i-1] and H[i] <= H[i+1]:
                    count += 1
        print(count)
