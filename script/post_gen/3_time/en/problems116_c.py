Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    h = list(map(int, input().split()))
    count = 0
    while max(h) > 0:
        for i in range(n):
            if h[i] > 0:
                count += 1
                while h[i] > 0:
                    h[i] -= 1
                    if i == n-1:
                        break
                    i += 1
    print(count)

=======
Suggestion 2

def solve(N, h):
    ans = 0
    for i in range(N - 1):
        if h[i] > h[i + 1]:
            ans += h[i] - h[i + 1]
    return ans

=======
Suggestion 3

def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    while max(h) > 0:
        l = 0
        while l < n and h[l] == 0:
            l += 1
        r = l
        while r < n and h[r] > 0:
            r += 1
        for i in range(l, r):
            h[i] -= 1
        ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    h = [int(x) for x in input().split()]
    count = 0
    while sum(h) > 0:
        l = 0
        r = 0
        for i in range(N):
            if h[i] > 0:
                l = i
                break
        for i in range(l, N):
            if h[i] == 0:
                r = i - 1
                break
        if r == 0:
            r = N - 1
        for i in range(l, r + 1):
            h[i] -= 1
        count += 1
    print(count)

=======
Suggestion 5

def main():
    n = int(input())
    h = [int(x) for x in input().split()]
    count = 0
    while (sum(h) != 0):
        for i in range(n):
            if h[i] != 0:
                count += 1
                while (i < n and h[i] != 0):
                    h[i] -= 1
                    i += 1
    print(count)

=======
Suggestion 6

def main():
    N = int(input())
    h = list(map(int, input().split()))
    ans = 0
    while True:
        if max(h) == 0:
            break
        else:
            left = 0
            while left < N:
                if h[left] == 0:
                    left += 1
                else:
                    break
            right = left
            while right < N:
                if h[right] != 0:
                    right += 1
                else:
                    break
            for i in range(left, right):
                h[i] -= 1
            ans += 1
    print(ans)

=======
Suggestion 7

def solve(N, h):
    count = 0
    while True:
        if max(h) == 0:
            break
        l = 0
        r = 0
        for i in range(N):
            if h[i] > 0:
                l = i
                break
        for i in range(l, N):
            if h[i] == 0:
                r = i - 1
                break
            elif i == N - 1:
                r = i
        for i in range(l, r + 1):
            h[i] -= 1
        count += 1
    return count

=======
Suggestion 8

def main():
    n = int(input())
    h = list(map(int, input().split()))
    #print(n, h)
    max_h = max(h)
    #print(max_h)
    count = 0
    while True:
        #print(h)
        if max_h == 0:
            break
        for i in range(n):
            if h[i] >= max_h:
                count += 1
                while True:
                    if i == n - 1:
                        break
                    if h[i+1] == 0:
                        break
                    i += 1
            else:
                while True:
                    if i == n - 1:
                        break
                    if h[i+1] == 0:
                        break
                    i += 1
        max_h -= 1
    print(count)

=======
Suggestion 9

def solve():
    n = int(input())
    h = [int(x) for x in input().split()]
    # print(n, h)
    count = 0
    for i in range(1, n):
        if h[i] < h[i-1]:
            count += h[i-1] - h[i]
    print(count)

=======
Suggestion 10

def read_int():
    return int(input())
