Synthesizing 10/10 solutions

=======
Suggestion 1

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
Suggestion 2

def main():
    N = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if i == 0:
            ans += h[i]
        else:
            if h[i-1] < h[i]:
                ans += h[i] - h[i-1]
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    h = list(map(int, input().split()))
    h.append(0)
    ans = 0
    for i in range(n):
        if h[i] < h[i+1]:
            ans += h[i+1] - h[i]
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    h = [int(x) for x in input().split()]
    ans = 0
    for i in range(N):
        if i == 0:
            ans += h[i]
        else:
            ans += abs(h[i] - h[i-1])
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    while True:
        if max(h) == 0:
            break
        for i in range(n):
            if h[i] == 0:
                continue
            else:
                h[i] -= 1
                if i == n-1:
                    count += 1
                    break
                elif i == 0:
                    if h[i+1] == 0:
                        count += 1
                        break
                elif h[i+1] == 0 and h[i-1] == 0:
                    count += 1
                    break
    print(count)

=======
Suggestion 6

def solve():
    N = int(input())
    h = list(map(int, input().split()))
    h.insert(0, 0)
    h.append(0)
    ans = 0
    for i in range(1, N+1):
        if h[i-1] < h[i]:
            ans += h[i] - h[i-1]
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    h = list(map(int,input().split()))
    cnt = 0
    while sum(h) > 0:
        for i in range(N):
            if h[i] > 0:
                cnt += 1
                h[i] -= 1
        # print(h)
    print(cnt)

=======
Suggestion 8

def main():
    N = int(input())
    h = list(map(int, input().split()))
    count = 0
    while True:
        if max(h) == 0:
            break
        else:
            for i in range(N):
                if h[i] > 0:
                    count += 1
                    h[i] -= 1
                else:
                    continue
    print(count)

=======
Suggestion 9

def main():
    N = int(input())
    h = list(map(int, input().split()))
    ans = 0
    while True:
        if max(h) == 0:
            break
        else:
            for i in range(N):
                if h[i] > 0:
                    ans += 1
                    h[i] -= 1
                else:
                    continue
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    h = list(map(int, input().split()))

    ans = 0
    while True:
        if max(h) == 0:
            break
        else:
            i = 0
            while i < n:
                if h[i] > 0:
                    ans += 1
                    while i < n and h[i] > 0:
                        h[i] -= 1
                        i += 1
                i += 1
    print(ans)
