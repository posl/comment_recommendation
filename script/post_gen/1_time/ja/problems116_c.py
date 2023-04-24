Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if h[i] > ans:
            ans = h[i]
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
    for i in range(1, N):
        if h[i] > h[i-1]:
            ans += h[i] - h[i-1]
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    h = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if h[i] > 0:
            count += 1
            for j in range(i+1, N):
                if h[j] > 0:
                    h[j] -= 1
    print(count)

=======
Suggestion 5

def main():
    N = int(input())
    h = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        if i == 0:
            ans += h[i]
        else:
            if h[i] > h[i-1]:
                ans += h[i] - h[i-1]
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    h = list(map(int, input().split()))
    ans = 0
    while max(h) > 0:
        l = 0
        r = 0
        for i in range(N):
            if h[i] > 0:
                l = i
                break
        for i in range(N - 1, -1, -1):
            if h[i] > 0:
                r = i
                break
        for i in range(l, r + 1):
            h[i] -= 1
        ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    h = list(map(int,input().split()))
    ans = 0
    while sum(h) > 0:
        i = 0
        while i < N:
            if h[i] > 0:
                j = i
                while j < N and h[j] > 0:
                    h[j] -= 1
                    j += 1
                ans += 1
            i += 1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    h = list(map(int, input().split()))
    ans = 0
    while 1:
        if max(h) == 0:
            break
        i = 0
        while 1:
            if i == N:
                break
            if h[i] != 0:
                break
            i += 1
        l = i
        while 1:
            if i == N:
                break
            if h[i] == 0:
                break
            i += 1
        r = i
        for j in range(l, r):
            h[j] -= 1
        ans += 1
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    H = list(map(int, input().split()))
    print(min([sum([abs(H[i] - H[j]) for j in range(N) if i != j]) for i in range(N)]))

=======
Suggestion 10

def main():
    N = int(input())
    h = list(map(int,input().split()))
    ans = 0
    while True:
        #print(h)
        if h == [0]*N:
            break
        l = 0
        r = 0
        for i in range(N):
            if h[i] != 0:
                l = i
                break
        for i in range(N-1,-1,-1):
            if h[i] != 0:
                r = i
                break
        for i in range(l,r+1):
            h[i] -= 1
        ans += 1
    print(ans)
