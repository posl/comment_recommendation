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
        if d <= x:
            ans += 1
        else:
            break
    print(ans)

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0] * (N + 1)
    for i in range(1, N + 1):
        D[i] = D[i - 1] + L[i - 1]
    cnt = 0
    for d in D:
        if d <= X:
            cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]
    for i in range(N):
        D.append(D[i] + L[i])
    ans = 0
    for i in range(N + 1):
        if D[i] <= X:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n,x = map(int,input().split())
    l = list(map(int,input().split()))
    cnt = 1
    d = 0
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
    count = 0
    for i in range(n):
        d += l[i]
        if d <= x:
            count += 1
    print(count + 1)

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]
    for i in range(N):
        D.append(D[i] + L[i])
    for i in range(N+1):
        if D[i] > X:
            print(i)
            break
    else:
        print(N+1)

=======
Suggestion 7

def solve():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    d = 0
    for i in range(n):
        d += l[i]
        if d > x:
            print(i + 1)
            return
    print(n + 1)

=======
Suggestion 8

def solve():
    N, X = [int(i) for i in input().split()]
    L = [int(i) for i in input().split()]
    D = 0
    ans = 1
    for i in range(N):
        D += L[i]
        if D <= X:
            ans += 1
    print(ans)

=======
Suggestion 9

def main():
    N, X = map(int, input().split())
    L_list = list(map(int, input().split()))
    cnt = 1
    D = 0
    for i in range(N):
        D = D + L_list[i]
        if D <= X:
            cnt = cnt + 1
    print(cnt)
