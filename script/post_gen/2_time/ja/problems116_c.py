Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        if h[i] > h[i - 1]:
            ans += h[i] - h[i - 1]
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    h = list(map(int,input().split()))
    ans = 0
    for i in range(1,N):
        if h[i-1] < h[i]:
            ans += h[i] - h[i-1]
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(max(h)):
        for j in range(N):
            if h[j] > 0:
                l = j
                break
        for j in range(N-1, -1, -1):
            if h[j] > 0:
                r = j
                break
        ans += 1
        for j in range(l, r+1):
            h[j] -= 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += h[i]
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    while True:
        i = 0
        while i < N:
            if H[i] == 0:
                i += 1
                continue
            l = i
            while i < N and H[i] > 0:
                i += 1
            r = i
            ans += 1
            for j in range(l, r):
                H[j] -= 1
        if i == N:
            break
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    h = list(map(int, input().split()))
    ans = 0
    while max(h) > 0:
        start = 0
        end = 0
        for i in range(N):
            if h[i] > 0:
                start = i
                break
        for i in range(N-1, -1, -1):
            if h[i] > 0:
                end = i
                break
        for i in range(start, end+1):
            h[i] -= 1
        ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i, N):
            if h[i] > h[j]:
                break
        else:
            ans += 1
    print(ans)

main()

=======
Suggestion 8

def main():
    N = int(input())
    h = list(map(int, input().split()))
    ans = 0
    while True:
        if all([i == 0 for i in h]):
            break
        for i in range(N):
            if h[i] != 0:
                l = i
                break
        for i in range(N-1, -1, -1):
            if h[i] != 0:
                r = i
                break
        for i in range(l, r+1):
            h[i] -= 1
        ans += 1
    print(ans)
