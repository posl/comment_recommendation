Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(n, k, x, a):
    a.sort()
    ans = 0
    for i in range(n):
        if k > 0:
            ans += max(a[i] - x, 0)
            k -= 1
        else:
            ans += a[i]
    return ans

=======
Suggestion 2

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    print(A)
    total = 0
    for i in range(N):
        if (K > 0):
            total += max(A[i] - X, 0)
            K -= 1
        else:
            total += A[i]
    print(total)

=======
Suggestion 3

def main():
    n,k,x = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    sum = 0
    for i in range(n):
        if k > 0:
            sum += max(a[i] - x,0)
            k -= 1
        else:
            sum += a[i]
    print(sum)

=======
Suggestion 4

def solve(N, K, X, A):
    ans = 0
    for i in range(N):
        if A[i] > X:
            ans += A[i] - X
    return ans

=======
Suggestion 5

def get_input():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    return n, k, x, a

=======
Suggestion 6

def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    sum = 0
    for i in range(n):
        if k > 0:
            if a[i] < x:
                sum += a[i]
                k -= 1
            else:
                sum += x
        else:
            sum += a[i]
    print(sum)

=======
Suggestion 7

def main():
    n,k,x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    #print(n,k,x)
    #print(a)
    sum = 0
    for i in range(n):
        if k>0:
            sum += max(a[i]-x,0)
            k -= 1
        else:
            sum += a[i]
    print(sum)

=======
Suggestion 8

def problem246_c():
    n,k,x = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    for i in range(n):
        if x <= 0:
            break
        if a[i] < x:
            a[i] = 0
            x -= 1
    print(sum(a))

problem246_c()

=======
Suggestion 9

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    total = 0
    for i in range(N):
        if K > 0:
            total += max(A[i] - X, 0)
            K -= 1
        else:
            total += A[i]
    print(total)

=======
Suggestion 10

def cal(a, x):
    if a < x:
        return 0
    else:
        return a - x
