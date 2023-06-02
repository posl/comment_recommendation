Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    a[x-1] = 0
    a = list(map(lambda x:x-1,a))
    #print(a)
    count = 0
    for i in range(n):
        if a[i] != -1:
            count += 1
            p = a[i]
            a[i] = -1
            while a[p] != -1:
                q = a[p]
                a[p] = -1
                p = q
    print(count)

=======
Suggestion 2

def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    a[x-1] = 0
    a = list(map(lambda x:x-1,a))
    b = [0]*n
    b[x-1] = 1
    for i in range(n):
        if b[i] == 1:
            b[a[i]] = 1
    print(sum(b))

=======
Suggestion 3

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a[x-1] = 0
    count = 1
    for i in range(n):
        if a[i] != 0:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    a[x-1] = 0
    ans = 1
    for i in range(n):
        if a[i] != 0:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    a[x-1] = 0
    b = [0]*n
    for i in range(n):
        if a[i] != 0:
            b[a[i]-1] += 1
    for i in range(n):
        if b[i] > 0:
            b[i] += 1
    print(sum(b))

=======
Suggestion 6

def solve():
    N,X = map(int,input().split())
    A = list(map(int,input().split()))
    A = [i-1 for i in A]
    B = [0]*N
    B[X-1] = 1
    for i in range(N):
        if B[A[i]] == 1:
            B[i] = 1
    print(sum(B))

=======
Suggestion 7

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    x -= 1
    b = [False] * n
    b[x] = True
    for i in range(n):
        if b[i]:
            b[a[i] - 1] = True
    print(b.count(True))

=======
Suggestion 8

def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    a = [a[i]-1 for i in range(n)]
    ans = 1
    y = x-1
    while a[y]!=x-1:
        ans+=1
        y = a[y]
    print(ans)

=======
Suggestion 9

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a[x-1] = 0
    a.sort()
    for i in range(n):
        if a[i] == 0:
            print(i)
            break
    else:
        print(n)

=======
Suggestion 10

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a - 1 for a in A]
    friends = [False] * N
    friends[X - 1] = True
    count = 1
    while True:
        if friends[A[X - 1]]:
            break
        friends[A[X - 1]] = True
        count += 1
        X = A[X - 1] + 1
    print(count)
