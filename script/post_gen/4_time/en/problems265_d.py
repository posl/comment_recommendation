Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if A[i] + A[j] + A[k] <= P:
                    ans = max(ans, (A[i] + A[j] + A[k]) * Q)
                else:
                    break
    print(ans)

=======
Suggestion 2

def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                for l in range(k+1,N):
                    ans = max(ans, P*A[i] + Q*A[j] + R*A[k])
    print(ans)

=======
Suggestion 3

def check(a, p, q, r):
    for i in range(1, len(a)):
        for j in range(i+1, len(a)):
            for k in range(j+1, len(a)):
                for l in range(k+1, len(a)):
                    if sum(a[i:j]) == p and sum(a[j:k]) == q and sum(a[k:l]) == r:
                        return True
    return False

n, p, q, r = map(int, input().split())
a = list(map(int, input().split()))

=======
Suggestion 4

def problems265_d():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    A = sorted(A, reverse=True)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                ans = max(ans, P*A[i]+Q*A[j]+R*A[k])
    print(ans)

=======
Suggestion 5

def solve():
    n,p,q,r = map(int, input().split())
    a = [int(x) for x in input().split()]
    a.sort()
    ans = 0
    for i in range(n):
        if a[i] >= p:
            break
        for j in range(i+1,n):
            if a[j] >= q:
                break
            for k in range(j+1,n):
                if a[k] >= r:
                    break
                for l in range(k+1,n):
                    if a[i] + a[j] + a[k] + a[l] == p + q + r:
                        ans += 1
    print("Yes" if ans else "No")

=======
Suggestion 6

def check_if_exists(a, p, q, r):
    n = len(a)
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    for i in range(n):
        for j in range(i + 2, n):
            for k in range(j + 2, n):
                for l in range(k + 2, n + 1):
                    if s[j] - s[i] == p and s[k] - s[j] == q and s[l] - s[k] == r:
                        return True
    return False

=======
Suggestion 7

def check(a,b,c,d):
    if a>b or b>c or c>d:
        return False
    if sum(A[a:b])!=P:
        return False
    if sum(A[b:c])!=Q:
        return False
    if sum(A[c:d])!=R:
        return False
    return True

=======
Suggestion 8

def main():
    #input
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))

    #compute
    A.sort()
    A.reverse()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                for l in range(k+1, N):
                    if A[i] + A[j] + A[k] == P and A[j] + A[k] + A[l] == Q and A[k] + A[l] + A[i] == R:
                        ans += 1
    if ans > 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    n,p,q,r = map(int, input().split())
    a = list(map(int, input().split()))

    #print(n,p,q,r)
    #print(a)

    a.sort()
    #print(a)

    sum_a = [0]*n
    sum_a[0] = a[0]
    for i in range(1, n):
        sum_a[i] = sum_a[i-1] + a[i]

    #print(sum_a)

    ans = 0
    for i in range(n):
        if (i+3) > n:
            break
        for j in range(i+1, n):
            if (j+2) > n:
                break
            for k in range(j+1, n):
                if (k+1) > n:
                    break
                if (sum_a[i] >= p) and (sum_a[j] >= q) and (sum_a[k] >= r):
                    ans += 1

    print(ans)

=======
Suggestion 10

def check(x,y,z,w):
    if x>=y or y>=z or z>=w:
        return False
    return True
