Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    p = list(map(int, input().split()))
    print(n)
    print(p)
    print(n)
    print(p)

=======
Suggestion 2

def main():
    n = int(input())
    p = list(map(int, input().split()))
    result = 0
    for i in range(n):
        if i == p[i]:
            result += 1
    if result == n:
        print(n)
        return
    for i in range(n):
        if i == p[i]:
            if i == n-1:
                if p[0] == 0:
                    result += 1
            else:
                if p[i+1] == 0:
                    result += 1
    print(result)

=======
Suggestion 3

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if p[i] == i:
            ans += 1
    if ans == n:
        print(n)
    else:
        print(ans+1)

=======
Suggestion 4

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if p[i] == i:
            ans += 1
            if i < n-1:
                p[i], p[i+1] = p[i+1], p[i]
            else:
                p[i], p[0] = p[0], p[i]
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    p = list(map(int, input().split()))
    p = [x-1 for x in p]
    count = 0
    for i in range(n):
        if p[i] == i:
            count += 1
            p[i] = -1
            if i != 0 and p[i-1] != -1:
                p[i-1] = -1
            elif i == 0 and p[n-1] != -1:
                p[n-1] = -1
            if i != n-1 and p[i+1] != -1:
                p[i+1] = -1
            elif i == n-1 and p[0] != -1:
                p[0] = -1
    print(count)

=======
Suggestion 6

def main():
    n = int(input())
    p = [int(x) for x in input().split()]
    ans = 0
    for i in range(n):
        if i == p[p[i]]:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    p = list(map(int, input().split()))
    for i in range(N):
        p[i] -= 1
    count = 0
    for i in range(N):
        if p[i] == i:
            count += 1
    if count == N:
        print(N)
        exit()
    count = 0
    for i in range(N):
        if p[i] == i:
            count += 1
    print(count)

=======
Suggestion 8

def main():
    N = int(input())
    P = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        if i == P[i]:
            ans += 1
            if i == N-1:
                P[0],P[i] = P[i],P[0]
            else:
                P[i+1],P[i] = P[i],P[i+1]
    print(ans)

main()

=======
Suggestion 9

def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if P[i] == i:
            ans += 1
            if i < N-1:
                P[i], P[i+1] = P[i+1], P[i]
            else:
                P[i], P[0] = P[0], P[i]
    print(ans)
