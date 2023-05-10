Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(1)
        return
    A = list(map(int, input().split()))
    A.sort()
    A.append(N+1)

    B = []
    for i in range(1,M+1):
        if A[i] - A[i-1] -1 != 0:
            B.append(A[i] - A[i-1] -1)
    if len(B) == 0:
        print(0)
        return
    K = min(B)
    ans = 0
    for b in B:
        ans += (b + K - 1) // K
    print(ans)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if m == 0:
        print(1)
        return
    if n == m:
        print(0)
        return
    b = [0] * (m + 1)
    for i in range(m):
        b[i + 1] = a[i] - a[i - 1] - 1
    b.sort()
    ans = 0
    for i in range(m - n + 1):
        ans += b[i]
    print(ans)

=======
Suggestion 3

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    if M == 0:
        print(1)
        return

    A.sort()

    if A[0] != 1:
        A.insert(0, 0)
    if A[M - 1] != N:
        A.append(N + 1)

    if M == 1:
        print(A[1] - A[0] - 1)
        return

    if M == 2:
        print(min(A[1] - A[0] - 1, A[2] - A[1] - 1))
        return

    ans = 0
    for i in range(1, M + 1):
        ans = max(ans, A[i] - A[i - 1] - 1)
    print(ans)

=======
Suggestion 4

def main():
    n,m = map(int,input().split())
    if m == 0:
        print(1)
        return
    a = list(map(int,input().split()))
    a.sort()
    a.append(n+1)
    l = []
    s = a[0]-1
    for i in range(1,m+1):
        if a[i]-a[i-1]-1 > 0:
            l.append(a[i]-a[i-1]-1)
    if len(l) == 0:
        print(0)
        return
    k = min(l)
    ans = 0
    for i in l:
        ans += (i+k-1)//k
    print(ans)

=======
Suggestion 5

def solve(n,m,as_):
    if m == 0:
        return 1
    if n == m:
        return 0
    as_.sort()
    diffs = []
    for i in range(m-1):
        diff = as_[i+1] - as_[i] - 1
        if diff > 0:
            diffs.append(diff)
    diff = as_[0] - 1
    if diff > 0:
        diffs.append(diff)
    diff = n - as_[-1]
    if diff > 0:
        diffs.append(diff)
    diffs.sort()
    k = diffs[0]
    ans = 0
    for diff in diffs:
        ans += (diff + k - 1) // k
    return ans

n,m = map(int, input().split())
as_ = list(map(int, input().split()))
print(solve(n,m,as_))

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if M == 0:
        print(1)
        exit()
    if N == M:
        print(0)
        exit()
    if N == 1:
        print(0)
        exit()
    if A[0] != 1:
        A = [0] + A
    if A[-1] != N:
        A = A + [N+1]
    if N == 2:
        if M == 1:
            print(1)
        else:
            print(0)
        exit()
    max_d = 0
    d = []
    for i in range(M):
        d.append(A[i+1] - A[i] - 1)
        if d[-1] > max_d:
            max_d = d[-1]
    if max_d == 0:
        print(0)
        exit()
    if max_d == 1:
        print(1)
        exit()
    if max_d % 2 == 0:
        print(max_d//2)
    else:
        print(max_d//2 + 1)
main()

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    if m == 0:
        print(1)
        return
    if n == m:
        print(0)
        return
    a = list(map(int,input().split()))
    a.sort()
    if m == 1:
        print(n-1)
        return
    d = []
    for i in range(1,m):
        d.append(a[i]-a[i-1]-1)
    d.sort()
    k = a[0]-1
    k += n-a[m-1]
    for i in range(m-1):
        k += d[i]
    print(k)

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    if m == 0:
        print(1)
        exit()
    if n == m:
        print(0)
        exit()
    b = []
    for i in range(m):
        if i == 0:
            b.append(a[i]-1)
        else:
            b.append(a[i]-a[i-1]-1)
    b.append(n-a[m-1])
    b.sort()
    k = b[0]
    ans = 0
    for i in range(m+1):
        if b[i] % k == 0:
            ans += b[i] // k
        else:
            ans += b[i] // k + 1
    print(ans)

=======
Suggestion 9

def main():
    N,M = map(int,input().split())
    if M == 0:
        print(1)
        return
    A = list(map(int,input().split()))
    A.sort()
    if A[0] != 1:
        A.insert(0,0)
    if A[-1] != N:
        A.append(N+1)
    k = N
    for i in range(len(A)-1):
        if A[i+1] - A[i] - 1 != 0:
            k = min(k,A[i+1] - A[i] - 1)
    ans = 0
    for i in range(len(A)-1):
        if A[i+1] - A[i] - 1 != 0:
            ans += (A[i+1] - A[i] - 1 + k - 1) // k
    print(ans)

=======
Suggestion 10

def main():
    n,m = map(int,input().split())
    if m == 0:
        print(1)
        return

    a = list(map(int,input().split()))
    a.sort()
    if a[0] != 1:
        a.insert(0,0)
    if a[-1] != n:
        a.append(n+1)
    
    if len(a) == 2:
        print(1)
        return
    
    if len(a) == 3:
        print(2)
        return
    
    k = []
    for i in range(1,len(a)):
        k.append(a[i]-a[i-1]-1)
    
    k = list(filter(lambda a: a != 0, k))
    k.sort()
    min_k = k[0]
    ans = 0
    for i in range(len(k)):
        ans += k[i]//min_k
        if k[i]%min_k != 0:
            ans += 1
    print(ans)
