Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    d = 0
    ans = 1
    for i in range(n):
        d += l[i]
        if d > x:
            break
        ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    d = 0
    ans = 1
    for i in range(n):
        d += l[i]
        if d <= x:
            ans += 1
        else:
            break
    print(ans)

=======
Suggestion 3

def main():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    d = 0
    ans = 1
    for i in range(n):
        d += l[i]
        if d <= x:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    d = 0
    cnt = 1
    for i in range(n):
        d += l[i]
        if d <= x:
            cnt += 1
    print(cnt)

=======
Suggestion 5

def main():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    d = 0
    cnt = 1
    for i in range(n):
        d += l[i]
        if d <= x:
            cnt += 1
        else:
            break
    print(cnt)

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0] * (N + 1)
    for i in range(N):
        D[i + 1] = D[i] + L[i]
    ans = 0
    for i in range(N + 1):
        if D[i] <= X:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]
    for i in range(1, N+1):
        D.append(D[i-1] + L[i-1])
    cnt = 0
    for i in range(N+1):
        if D[i] <= X:
            cnt += 1
    print(cnt)

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))

    ans = 1
    pos = 0
    for i in range(N):
        pos += L[i]
        if pos <= X:
            ans += 1
        else:
            break
    print(ans)

=======
Suggestion 9

def solve():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = 0
    for i in range(1, N + 1):
        D += L[i - 1]
        if D > X:
            print(i)
            return
    print(N + 1)
