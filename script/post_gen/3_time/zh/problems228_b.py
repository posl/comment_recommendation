Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a = list(map(lambda x: x-1, a))
    print(len(set(a) | {x-1}))
    return

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A[X-1] = 0
    A.sort()
    A = A[::-1]
    count = 0
    for i in range(N):
        if A[i] != 0:
            count += 1
        else:
            break
    print(count)

=======
Suggestion 3

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a = [i-1 for i in a]
    cnt = 1
    i = x
    while a[i] != x:
        cnt += 1
        i = a[i]
    print(cnt)

main()

=======
Suggestion 4

def main():
    N,X = map(int,input().split())
    A = list(map(int,input().split()))
    A.insert(0,0)
    B = [0]*(N+1)
    B[X] = 1
    for i in range(1,N+1):
        if B[i] == 1:
            B[A[i]] = 1
    print(B.count(1))

=======
Suggestion 5

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a[x - 1] = 0
    for i in range(n):
        if a[i] == x:
            a[i] = 0
    print(len(set(a)))

=======
Suggestion 6

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a = [i - 1 for i in a]
    b = [0] * n
    for i in range(n):
        b[a[i]] += 1
    if b[x - 1] == 0:
        print(0)
        return
    b[x - 1] = 0
    for i in range(n):
        if b[i] > 0:
            print(b[i] + 1)

=======
Suggestion 7

def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    a[x-1] = 0
    for i in range(n):
        if a[i] != 0:
            a[a[i]-1] = 0
    print(n - a.count(0))

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A = [x - 1 for x in A]
    share = [0] * N
    share[X - 1] = 1
    for i in range(N):
        share[A[i]] += share[i]
    print(sum(share))

=======
Suggestion 9

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    x -= 1
    a[x] = 0
    ans = 1
    for i in range(n):
        if a[i] != 0:
            ans += 1
    print(ans)

=======
Suggestion 10

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] -= 1
    b = [0] * n
    b[x - 1] = 1
    for i in range(n):
        b[a[i]] += 1
    ans = 0
    for i in range(n):
        if b[i] > 1:
            ans += 1
    print(ans)
