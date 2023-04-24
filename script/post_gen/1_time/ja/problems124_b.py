Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 1
    for i in range(1, N):
        if H[i-1] <= H[i]:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 1
    for i in range(N-1):
        if H[i] <= H[i+1]:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 1
    for i in range(1, n):
        if h[i - 1] <= h[i]:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if i == 0:
            count += 1
        else:
            if H[i-1] <= H[i]:
                count += 1
    print(count)

=======
Suggestion 5

def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if i == 0:
            ans += 1
        else:
            if h[i-1] <= h[i]:
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    h = list(map(int, input().split()))

    count = 1
    for i in range(1, n):
        if h[i] >= max(h[:i]):
            count += 1

    print(count)

=======
Suggestion 7

def main():
    N = int(input())
    H = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if i == 0:
            cnt += 1
        else:
            if max(H[:i]) <= H[i]:
                cnt += 1
    print(cnt)

=======
Suggestion 8

def main():
    N = int(input())
    H = [int(i) for i in input().split()]
    count = 0
    for i in range(N):
        if i == 0:
            count += 1
            continue
        for j in range(i):
            if H[i] < H[j]:
                break
        else:
            count += 1
    print(count)

=======
Suggestion 9

def main():
    N = int(input())
    H = list(map(int, input().split()))

    result = 0
    for i in range(N):
        if i == 0:
            result += 1
            continue
        if H[i-1] <= H[i]:
            result += 1
    print(result)
