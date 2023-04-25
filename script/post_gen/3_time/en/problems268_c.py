Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if p[i] == i:
            ans += 1
            if i < n-1:
                p[i+1], p[i] = p[i], p[i+1]
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if p[i] == i:
            ans += 1
            if i < n-1:
                p[i+1], p[i] = p[i], p[i+1]
            else:
                p[i-1], p[i] = p[i], p[i-1]
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if p[i] == i:
            ans += 1
            if i < n - 1 and p[i + 1] == i + 1:
                p[i], p[i + 1] = p[i + 1], p[i]
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if p[i] == i:
            count += 1
    if count == N:
        print(N)
    else:
        print(N - 1)

=======
Suggestion 5

def main():
    N = int(input())
    p = list(map(int, input().split()))
    happy = 0
    for i in range(N):
        if p[i] == (i-1)%N or p[i] == i or p[i] == (i+1)%N:
            happy += 1
    print(happy)

=======
Suggestion 6

def main():
    N = int(input())
    P = list(map(int,input().split()))
    cnt = 0
    for i in range(N):
        if P[i] == i:
            cnt += 1
            if i < N-1:
                P[i+1] = i+1
            else:
                P[0] = 0
    print(cnt)

=======
Suggestion 7

def main():
    N = int(input())
    P = list(map(int, input().split()))
    happy = 0

    for i in range(1, N-1):
        if P[i-1] < P[i] < P[i+1] or P[i-1] > P[i] > P[i+1]:
            happy += 1
    if P[N-2] < P[N-1] < P[0] or P[N-2] > P[N-1] > P[0]:
        happy += 1
    if P[N-1] < P[0] < P[1] or P[N-1] > P[0] > P[1]:
        happy += 1

    print(happy)

=======
Suggestion 8

def main():
    N = int(input())
    P = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if i == 0:
            if P[i] == N - 1 or P[i] == 1:
                count += 1
        elif i == N - 1:
            if P[i] == N - 2 or P[i] == 0:
                count += 1
        else:
            if P[i] == P[i - 1] - 1 or P[i] == P[i - 1] + 1:
                count += 1
    print(count)

=======
Suggestion 9

def main():
    N = int(input())
    p = [int(x) for x in input().split()]
    p = [x-1 for x in p]
    count = 0
    for i in range(N):
        if p[p[i]] == i:
            count += 1
    print(count)

=======
Suggestion 10

def get_input():
    n = int(input())
    p = [int(i) for i in input().split()]
    return n, p
