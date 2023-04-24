Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if p[i] == i:
            ans += 1
            if i < N-1:
                p[i], p[i+1] = p[i+1], p[i]
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if p[i] == i:
            ans += 1
            if i != N-1:
                p[i], p[i+1] = p[i+1], p[i]
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if p[i] == i:
            if i == 0:
                p[i], p[i+1] = p[i+1], p[i]
            elif i == N-1:
                p[i], p[i-1] = p[i-1], p[i]
            else:
                p[i], p[i+1] = p[i+1], p[i]
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if P[i] == i:
            ans += 1
            if i < N - 1:
                P[i], P[i + 1] = P[i + 1], P[i]
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    p = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if p[i] == i:
            cnt += 1
    print(cnt // 2 + cnt % 2)
main()

=======
Suggestion 6

def main():
    n = int(input())
    p = list(map(int,input().split()))
    ans = 0
    for i in range(1,n-1):
        if p[i-1] == i-1 or p[i] == i or p[i+1] == i+1:
            ans += 1
    if p[0] == 0 or p[n-1] == n-1 or p[n-2] == n-2:
        ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    P = list(map(i

=======
Suggestion 8

def main():
    N = int(input())
    P = list(map(int, input().split()))
    for i in range(N):
        P[i] = (P[i] - i) % N
    #print(P)
    cnt = [0] * N
    for p in P:
        cnt[p] += 1
    #print(cnt)
    print(max(cnt))

=======
Suggestion 9

def main():
    N = int(input())
    P = [int(x) for x in input().split()]
    #print(N)
    #print(P)
    P2 = [0] * N
    for i in range(N):
        P2[P[i]] = i
    #print(P2)
    ans = 1
    cnt = 1
    for i in range(1, N):
        if P2[i] < P2[i-1]:
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 1
    ans = max(ans, cnt)
    print(ans)
