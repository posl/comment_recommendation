Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if A[i] != X:
            count += 1
            X = A[i]
    print(count)

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a = [i for i in a if i != x]
    print(len(a))

=======
Suggestion 3

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a[x-1] = 0
    count = 1
    for i in range(n):
        if a[i] == 0:
            continue
        else:
            count += 1
            a[a[i]-1] = 0
    print(count)

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    count = 1
    while True:
        if A[X-1] == X:
            break
        else:
            X = A[X-1]
            count += 1
    print(count)

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A[X-1] = 0
    print(len(set(A)))

=======
Suggestion 6

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a = [i - 1 for i in a]
    b = [False] * n
    b[x - 1] = True
    for i in range(n):
        if b[i]:
            b[a[i]] = True
    print(sum(b))

=======
Suggestion 7

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(x-1, 0)
    a = list(map(lambda x: x-1, a))
    cnt = 1
    i = x-1
    while True:
        i = a[i]
        if i == 0:
            break
        cnt += 1
    print(cnt)

=======
Suggestion 8

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a[x-1] = 0
    print(a.count(1))

=======
Suggestion 9

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    
    ans = 0
    for i in range(1, n+1):
        if x == i:
            continue
        if a[i] == x:
            ans += 1
            continue
        if a[a[i]] == x:
            ans += 1
            continue
    print(ans)

=======
Suggestion 10

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(X)
    A.sort()
    count = 1
    for i in range(1, N):
        if A[i-1] != A[i]:
            count += 1
    print(count)
