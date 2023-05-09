Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-3):
        for j in range(i+1, N-2):
            for k in range(j+1, N-1):
                for l in range(k+1, N):
                    if (A[i] + A[j] + A[k] == P) and (A[i] + A[j] + A[l] == Q) and (A[i] + A[k] + A[l] == R) and (A[j] + A[k] + A[l] == R):
                        ans += 1
    if ans > 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    n,p,q,r = map(int,input().split())
    a = list(map(int,input().split()))

    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    if p == sum(a[i:j]) and q == sum(a[j:k]) and r == sum(a[k:l]):
                        ans += 1
    if ans > 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def solve():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans = max(ans, P * A[i] + Q * A[i] + R * A[i])
    print(ans)

=======
Suggestion 4

def main():
    N,P,Q,R = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                for l in range(k+1,N):
                    if A[i]+A[j]+A[k] == P and A[j]+A[k]+A[l] == Q and A[k] == R:
                        ans += 1
    if ans > 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(1, N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if P == A[i] + A[i-1] and Q == A[j] + A[j-1] and R == A[k] + A[k-1]:
                    ans += 1
    if ans > 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    n,p,q,r = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n-3):
        for j in range(i+1,n-2):
            for k in range(j+1,n-1):
                for l in range(k+1,n):
                    if p == sum(a[i:j+1]) and q == sum(a[j:k+1]) and r == sum(a[k:l+1]):
                        ans += 1
    if ans > 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def solve():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if i >= 3:
            break
        for j in range(i+1, N):
            if j >= 3:
                break
            for k in range(j+1, N):
                if k >= 3:
                    break
                for l in range(k+1, N):
                    if l >= 3:
                        break
                    ans = max(ans, P*A[i]+Q*A[j]+R*A[k])
    print(ans)
    return 0

=======
Suggestion 8

def main():
    n, p, q, r = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0

    for i in range(n):
        if a[i] > r:
            break
        for j in range(i, n):
            if a[j] > q:
                break
            for k in range(j, n):
                if a[k] > p:
                    break
                for l in range(k, n):
                    if a[l] > r:
                        break
                    if i <= j <= k <= l:
                        if a[i] + a[j] + a[k] == p and a[j] + a[k] + a[l] == q and a[i] + a[k] + a[l] == r:
                            ans += 1
    if ans > 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    n, p, q, r = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(n):
        a = A[i]
        if a > r:
            break
        for j in range(i+1,n):
            b = A[j]
            if b > r:
                break
            for k in range(j+1,n):
                c = A[k]
                if c > r:
                    break
                for l in range(k+1,n):
                    d = A[l]
                    if d > r:
                        break
                    if a+b+c == p and b+c+d == q and c+d+a == r:
                        print('Yes')
                        return
    print('No')
    return

=======
Suggestion 10

def check_sum(a, p, q, r):
    if sum(a[0:p]) == p and sum(a[p:q]) == q and sum(a[q:r]) == r:
        return True
    else:
        return False
