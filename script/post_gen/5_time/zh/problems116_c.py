Synthesizing 10/10 solutions

=======
Suggestion 1

def min_watering(h):
    count = 0
    for i in range(len(h)):
        if h[i] == 0:
            continue
        elif i == len(h)-1:
            count += h[i]
        else:
            count += h[i]
            if h[i] <= h[i+1]:
                count += h[i]
            else:
                count += h[i+1]
    return count

=======
Suggestion 2

def solve(n,h):
    ans = 0
    for i in range(1,n+1):
        if h[i-1] == 0:
            continue
        else:
            ans += h[i-1]
            if i != n:
                if h[i] != 0:
                    ans += h[i-1]
    return ans

=======
Suggestion 3

def solve():
    n = int(input())
    h = list(map(int, input().split()))
    h.insert(0, 0)
    ans = 0
    for i in range(1, n + 1):
        if h[i] > h[i - 1]:
            ans += h[i] - h[i - 1]
    print(ans)

solve()

=======
Suggestion 4

def main():
    n = int(input())
    h = list(map(int,input().split()))
    h.insert(0,0)
    h.append(0)
    ans = 0
    for i in range(1,n+1):
        if h[i-1] < h[i] and h[i] > h[i+1]:
            ans += 1
        if h[i-1] > h[i] and h[i] < h[i+1]:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    h = list(map(int, input().split()))
    ans = 0
    while sum(h) > 0:
        for i in range(N):
            if h[i] > 0:
                ans += 1
                h[i] -= 1
                while i < N and h[i] > 0:
                    h[i] -= 1
                    i += 1
                break
    print(ans)

=======
Suggestion 6

def water_flowers(N, h):
    return 0

=======
Suggestion 7

def solve(n, h):
    ans = 0
    while True:
        left = -1
        right = -1
        for i in range(n):
            if h[i] > 0:
                if left == -1:
                    left = i
                right = i
        if left == -1:
            break
        for i in range(left, right+1):
            h[i] -= 1
        ans += 1
    return ans

n = int(input())
h = list(map(int, input().split()))
print(solve(n, h))

=======
Suggestion 8

def main():
    N = int(input())
    h = list(map(int, input().split()))
    h.insert(0, 0)
    h.append(0)
    count = 0
    for i in range(1,N+2):
        if h[i] > h[i-1]:
            count += h[i] - h[i-1]
    print(count)

=======
Suggestion 9

def get_min_watering_times(N, h):
    water_times = 0
    for i in range(N):
        if h[i] == 0:
            continue
        elif h[i] == 1:
            water_times += 1
        else:
            water_times += h[i]
    return water_times

=======
Suggestion 10

def main():
    n = int(input())
    h = list(map(int,input().split()))
    h.insert(0,0)
    ans = 0
    for i in range(1,n+1):
        if h[i-1] < h[i]:
            ans += h[i] - h[i-1]
    print(ans)
