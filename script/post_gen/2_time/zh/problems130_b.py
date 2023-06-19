Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))

    # print(N, X, L)
    D = [0]*(N+1)
    for i in range(1, N+1):
        D[i] = D[i-1] + L[i-1]
    # print(D)
    cnt = 0
    for i in range(N+1):
        if D[i] <= X:
            cnt += 1
    print(cnt)

=======
Suggestion 2

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

main()

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))

    ans = 1
    d = 0
    for i in range(N):
        d += L[i]
        if d <= X:
            ans += 1

    print(ans)

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]
    for i in range(N):
        D.append(D[i] + L[i])
    ans = 0
    for i in range(N+1):
        if D[i] <= X:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    n,x = map(int, input().split())
    l = list(map(int, input().split()))
    d = 0
    count = 1
    for i in range(n):
        if d <= x:
            d += l[i]
            count += 1
    print(count)

=======
Suggestion 6

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
Suggestion 7

def count_bounce_times(N, X, L):
    D = [0] * (N + 1)
    D[0] = 0
    for i in range(1, N + 1):
        D[i] = D[i - 1] + L[i - 1]
    count = 0
    for d in D:
        if d <= X:
            count += 1
    return count

=======
Suggestion 8

def problems130_b():
    n,x = map(int,input().split())
    l = list(map(int,input().split()))
    d = [0]
    for i in range(n):
        d.append(d[i]+l[i])
    count = 0
    for i in d:
        if i <= x:
            count += 1
    print(count)

=======
Suggestion 9

def main():
    n,x = map(int,input().split())
    l = list(map(int,input().split()))
    d = [0]*(n+1)
    for i in range(1,n+1):
        d[i] = d[i-1]+l[i-1]
    ans = 0
    for i in range(n+1):
        if d[i]<=x:
            ans += 1
    print(ans)

=======
Suggestion 10

def main():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    d = 0
    count = 1
    for i in range(n):
        d += l[i]
        if d <= x:
            count += 1
    print(count)
