Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    p = [int(i)-1 for i in input().split()]
    ans = 0
    for i in range(n):
        if p[i] == i:
            ans += 1
            if i == n-1:
                p[i], p[0] = p[0], p[i]
            else:
                p[i], p[i+1] = p[i+1], p[i]
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(n-1):
        if p[i] == i:
            p[i], p[i+1] = p[i+1], p[i]
            count += 1
    if p[-1] == n-1:
        count += 1
    print(count)

=======
Suggestion 3

def main():
    N = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if p[i] == i:
            if i == N-1:
                p[i], p[0] = p[0], p[i]
            else:
                p[i], p[i+1] = p[i+1], p[i]
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    p = [int(x) for x in input().split()]
    ans = 0
    for i in range(N):
        if p[i] == i:
            ans += 1
            if i+1 < N and p[i+1] == i+1:
                p[i+1] = p[i]
            else:
                p[i-1] = p[i]
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    p = list(map(int, input().split()))
    c = 0
    for i in range(n):
        if p[i] == i:
            c += 1
    if c == n:
        print(n)
    else:
        print(n-1)

=======
Suggestion 6

def main():
    n = int(input())
    p = [int(i) for i in input().split()]
    count = 0
    for i in range(n):
        if p[i] == i:
            if i == n-1:
                p[i], p[i-1] = p[i-1], p[i]
            else:
                p[i], p[i+1] = p[i+1], p[i]
            count += 1
    print(count)

=======
Suggestion 7

def main():
    n = int(input())
    p = [int(i) for i in input().split()]
    happy = 0
    for i in range(n):
        if i == 0:
            if p[i] == n-1 or p[i] == 1:
                happy += 1
        elif i == n-1:
            if p[i] == n-2 or p[i] == 0:
                happy += 1
        else:
            if p[i] == i-1 or p[i] == i+1:
                happy += 1
    print(happy)

=======
Suggestion 8

def solve(n, p):
    ans = 0
    for i in range(n):
        if i == p[p[i]]:
            ans += 1
    return ans

=======
Suggestion 9

def main():
    n = int(input())
    p = list(map(int, input().split()))

    # 0 1 2 3
    # 1 2 0 3
    # 2 0 3 1
    # 3 1 2 0

    # 0 1 2 3 4 5 6 7 8 9
    # 3 9 6 1 7 2 8 0 5 4
    # 1 7 4 9 5 0 6 8 3 2
    # 7 4 9 5 0 6 8 3 2 1
    # 4 9 5 0 6 8 3 2 1 7
    # 9 5 0 6 8 3 2 1 7 4
    # 5 0 6 8 3 2 1 7 4 9
    # 0 6 8 3 2 1 7 4 9 5
    # 6 8 3 2 1 7 4 9 5 0
    # 8 3 2 1 7 4 9 5 0 6
    # 3 2 1 7 4 9 5 0 6 8
    # 2 1 7 4 9 5 0 6 8 3

    # 0 1 2 3 4 5 6 7 8 9
    # 1 7 4 9 5 0 6 8 3 2
    # 7 4 9 5 0 6 8 3 2 1
    # 4 9 5 0 6 8 3 2 1 7
    # 9 5 0 6 8 3 2 1 7 4
    # 5 0 6 8 3 2 1 7 4 9
    # 0 6 8 3 2 1 7 4 9 5

=======
Suggestion 10

def solve():
    pass
