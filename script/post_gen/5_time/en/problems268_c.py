Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if p[i] == i:
            ans += 1
            if i < N-1 and p[i+1] == i+1:
                p[i], p[i+1] = p[i+1], p[i]
            elif i == N-1:
                p[i], p[0] = p[0], p[i]
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if p[i] == i:
            count += 1
            if i < N-1 and p[i+1] == i+1:
                p[i], p[i+1] = p[i+1], p[i]
            elif i == N-1:
                p[i], p[0] = p[0], p[i]
    print(count)

=======
Suggestion 3

def solve():
    N = int(input())
    P = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        if P[i] == i:
            ans += 1
            if i < N-1 and P[i+1] == i+1:
                P[i], P[i+1] = P[i+1], P[i]
            elif i == N-1 and P[0] == 0:
                P[i], P[0] = P[0], P[i]
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(len(p)):
        if p[i] == i:
            count += 1
    if count == len(p):
        print(count)
    else:
        count = 0
        for i in range(len(p)):
            if p[i] == i:
                count += 1
            else:
                if p[p[i]] == i:
                    count += 1
        print(count)

=======
Suggestion 5

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if p[i] == i:
            count += 1
            if i + 1 < n:
                p[i], p[i+1] = p[i+1], p[i]
            else:
                p[i], p[0] = p[0], p[i]
    print(count)

=======
Suggestion 6

def main():
    N = int(input())
    p = list(map(int, input().split()))
    happy = 0
    for i in range(N):
        if p[i] == i:
            happy += 1
            if i < N-1 and p[i+1] == i+1:
                p[i], p[i+1] = p[i+1], p[i]
            elif i == N-1:
                p[i], p[0] = p[0], p[i]
    print(happy)

=======
Suggestion 7

def main():
    N = int(input())
    p = list(map(int, input().split()))
    q = [0]*N
    for i in range(N):
        q[p[i]] = i
    ans = 0
    cnt = 0
    for i in range(N):
        if q[i] > cnt:
            cnt = q[i]
        else:
            ans += 1
    print(ans)
    
main()

=======
Suggestion 8

def main():
    n = int(input())
    p = [int(x) for x in input().split()]
    p.insert(0,0)
    p.append(0)
    count = 0
    for i in range(1,n+1):
        if p[i] == i-1:
            count += 1
            p[i] = i
            p[i+1] = i+1
    print(count)

=======
Suggestion 9

def main():
    N = int(input())
    P = list(map(int, input().split()))
    print(N)

=======
Suggestion 10

def main():
    return
