Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    P = list(map(int, input().split()))
    P = [p-1 for p in

=======
Suggestion 2

def main():
    N = int(input())
    p = list(map(int, input().split()))
    p.insert(0, 0)
    p.insert(N+1, 0)
    ans = 0
    for i in range(1, N+1):
        if (p[i-1] < p[i] < p[i+1]) or (p[i+1] < p[i] < p[i-1]):
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    p = [int(x) for x in input().split()]
    p = [x-1 for x in p]
    ans = 0
    for i in range(n):
        if p[i] == i:
            ans += 1
            if i < n-1:
                p[i], p[i+1] = p[i+1], p[i]
            else:
                p[0], p[i] = p[i], p[0]
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    p = [int(i) for i in input().split()]
    happy = 0
    for i in range(N):
        if p[i] == (p[(i-1)%N]+1)%N or p[i] == (p[(i+1)%N]-1)%N:
            happy += 1
    print(happy)

=======
Suggestion 5

def main():
    N = int(input())
    p = list(map(int, input().split()))
    p = [x - 1 for x in p]
    res = 0
    for i in range(N):
        if p[i] == i:
            res += 1
            if i < N - 1:
                p[i], p[i + 1] = p[i + 1], p[i]
            else:
                p[i], p[0] = p[0], p[i]
    print(res)

=======
Suggestion 6

def main():
    n = int(input())
    ps = list(map(int, input().split()))
    ps = [p-1 for p in ps]
    # print(ps)
    cnt = 0
    for i in range(n):
        if ps[ps[ps[i]]] == i:
            cnt += 1
    print(cnt//2)

=======
Suggestion 7

def main():
    N = int(input())
    p = list(map(int, input().split()))
    p = [x-1 for x in p]
    ans = 0
    for i in range(N):
        if (p[p[i]] == i):
            ans += 1
    print(ans//2)

=======
Suggestion 8

def solve():
    N = int(input())
    P = [int(i) for i in input().split()]

    # 0 1 2 3
    # 1 2 0 3
    # 2 0 3 1
    # 3 1 2 0

    # 0 1 2 3 4 5 6 7 8 9
    # 3 9 6 1 7 2 8 0 5 4
    # 6 1 7 2 8 0 5 4 3 9
    # 7 2 8 0 5 4 3 9 6 1
    # 8 0 5 4 3 9 6 1 7 2
    # 5 4 3 9 6 1 7 2 8 0
    # 3 9 6 1 7 2 8 0 5 4
    # 6 1 7 2 8 0 5 4 3 9
    # 7 2 8 0 5 4 3 9 6 1
    # 8 0 5 4 3 9 6 1 7 2

    # 0 1 2 3 4 5 6 7 8 9
    # 3 9 6 1 7 2 8 0 5 4
    # 6 1 7 2 8 0 5 4 3 9
    # 7 2 8 0 5 4 3 9 6 1
    # 8 0 5 4 3 9 6 1 7 2
    # 5 4 3 9 6 1 7 2 8 0
    # 3 9 6 1 7 2 8 0 5 4
    # 6 1 7 2 8 0 5 4 3 9
    # 7 2 8 0 5 4 3 9 6

=======
Suggestion 9

def main():
    N = int(input())
    P = list(map(int, input().split()))

    # 逆時針の転回回数を求める
    cnt = 0
    for i in range(N):
        if P[i] == i:
            cnt += 1

    if cnt == N:
        print(N)
    else:
        print(cnt + 2 * ((N - cnt) // 2))

=======
Suggestion 10

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if p[i] == (i - 1) % n or p[i] == i or p[i] == (i + 1) % n:
            ans += 1
    print(ans)
