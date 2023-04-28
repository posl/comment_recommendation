Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a[x-1] = 0
    ans = 1
    for i in range(n):
        if a[i] != 0:
            ans += 1
            a[a[i]-1] = 0
    print(ans)

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    count = 0
    for i in range(n):
        if a[i] <= x:
            count += 1
            x -= a[i]
        else:
            break
    if x > 0 and count == n:
        count -= 1
    print(count)

=======
Suggestion 3

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a[x-1] = 0
    b = [0] * n
    for i in range(n):
        if a[i] != 0:
            b[a[i]-1] += 1
    print(b.count(max(b)))

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a = [i - 1 for i in a]
    b = [0] * n
    b[x - 1] = 1
    ans = 1
    for i in range(n):
        if b[a[i]] == 1:
            ans += 1
            b[i] = 1
    print(ans)

=======
Suggestion 5

def solve():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    x -= 1
    ans = 1
    while x != a[x]:
        x = a[x]
        ans += 1
        if ans > n:
            ans = -1
            break
    print(ans)

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    friends = [0] * (N + 1)
    friends[X] = 1
    for i in range(1, N + 1):
        if friends[i] == 1:
            friends[A[i]] = 1
    print(sum(friends))
main()

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a - 1 for a in A]
    cnt = 1
    x = X - 1
    while A[x] != X - 1:
        x = A[x]
        cnt += 1
        if cnt > N:
            print(-1)
            return
    print(cnt)

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))

    A.append(X)

    friends = [0] * N
    friends[X - 1] = 1

    for i in range(N):
        if friends[i] == 1:
            friends[A[i] - 1] = 1

    print(sum(friends))

main()

=======
Suggestion 9

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a = [x-1 for x in a]
    #print(a)
    #print(n)
    #print(x)
    #print(a)
    b = [0]*n
    b[x-1] = 1
    #print(b)
    for i in range(n):
        if b[i] == 1:
            b[a[i]] = 1
    #print(b)
    print(sum(b))

=======
Suggestion 10

def main():
    N,X = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N,X,A)
    ans = 0
    for i in range(N):
        if X == A[i]:
            ans += 1
    print(ans)

main()
