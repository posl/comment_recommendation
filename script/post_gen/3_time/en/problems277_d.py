Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = [0] * m
    for i in range(n):
        b[a[i]] += 1
    ans = 0
    for i in range(m):
        if b[i] > 1:
            b[i+1] += b[i] - 1
        elif b[i] == 0:
            ans += i
            break
    for i in range(m-1, -1, -1):
        if b[i] == 0:
            ans += m - 1 - i
            break
    print(ans)

=======
Suggestion 2

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    B = []
    for i in range(N):
        if i == 0:
            B.append(A[i])
        else:
            if A[i] != B[-1]:
                B.append(A[i])
    N = len(B)
    if N == 1:
        print(0)
        exit()
    B.append(B[0]+M)
    C = []
    for i in range(N):
        C.append(B[i+1]-B[i]-1)
    C.sort()
    print(sum(C[:N-1]))

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.append(m)
    b = [a[0]]
    for i in range(1, n+1):
        if a[i] == a[i-1]:
            continue
        b.append(a[i])
    n = len(b)
    c = [0] * n
    for i in range(n):
        c[i] = b[i] - b[i-1] - 1
    ans = 0
    for i in range(n):
        ans += (c[i] + 1) // 2
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i]
    print(ans - A[-1])

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = [0]*(m+1)
    for i in a:
        b[i] = b[i-1] + 1
    print(n - max(b))
main()

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A_list = list(map(int, input().split()))
    A_list.sort()
    A_list.

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.append(m)
    ans = 0
    pre = 0
    for i in range(n+1):
        ans += (a[i]-pre-1)//(n+1)
        pre = a[i]
    print(ans)

=======
Suggestion 8

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.append(m)
    b = []
    prev = -1
    for i in range(n + 1):
        if a[i] != prev:
            b.append([a[i], 1])
            prev = a[i]
        else:
            b[-1][1] += 1
    c = [0] * len(b)
    for i in range(len(b) - 1):
        c[i + 1] = c[i] + b[i][1]
    ans = 0
    for i in range(len(b)):
        if b[i][0] - c[i] > 0:
            ans += b[i][0] - c[i]
    print(ans)

=======
Suggestion 9

def main():
    # input
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # compute
    A.sort()
    A.append(M)
    B = []
    prev = -1
    count = 0
    for a in A:
        if a == prev:
            count += 1
        else:
            if prev != -1:
                B.append(count)
            count = 1
            prev = a
    B.sort(reverse=True)
    if len(B) == 1:
        ans = B[0]
    elif len(B) == 2:
        ans = B[0] + B[1]
    else:
        ans = B[0] + B[1] + B[2]
    ans = N - ans
    print(ans)

=======
Suggestion 10

def count(n, m, a):
    count = [0] * m
    for i in range(n):
        count[a[i]] += 1
    return count
