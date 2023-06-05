Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int,input().split())
    L = list(map(int,input().split()))
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
Suggestion 2

def main():
    n,x = map(int,input().split())
    l = list(map(int,input().split()))
    d = 0
    cnt = 1
    for i in range(n):
        d += l[i]
        if d <= x:
            cnt += 1
    print(cnt)

=======
Suggestion 3

def get_input():
    n,x = map(int, input().split())
    L = list(map(int, input().split()))
    return n,x,L

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    d = [0]
    for i in range(n):
        d.append(d[i] + l[i])
    for i in range(n+1):
        if d[i] > x:
            print(i)
            return
    print(n+1)

=======
Suggestion 5

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
Suggestion 6

def solution():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0 for i in range(N+1)]
    D[0] = 0
    for i in range(1,N+1):
        D[i] = D[i-1]+L[i-1]
    for i in range(N+1):
        if D[i] > X:
            print(i)
            break
    else:
        print(N+1)

=======
Suggestion 7

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

=======
Suggestion 8

def main():
    N,X = map(int,input().split())
    L = list(map(int,input().split()))
    D = [0]*(N+1)
    for i in range(N):
        D[i+1] = D[i]+L[i]
    D.append(D[N]+L[N-1])
    for i in range(N+1):
        if D[i]>X:
            print(i)
            break
    else:
        print(N+1)

=======
Suggestion 9

def problems130_b():
    n,x = map(int,input().split())
    l = list(map(int,input().split()))
    d = 0
    count = 1
    for i in range(n):
        d += l[i]
        if d <= x:
            count += 1
    print(count)

problems130_b()

=======
Suggestion 10

def main():
    (N,X) = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]*(N+1)
    for i in range(1,N+1):
        D[i] = D[i-1] + L[i-1]
    i = 0
    while D[i] <= X:
        i += 1
    print(i)
