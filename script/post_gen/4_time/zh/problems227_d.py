Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = []
    for i in range(n - 1):
        b.append(a[i + 1] - a[i])
    b.sort()
    print(sum(b[:n - k]))

=======
Suggestion 2

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    a = a[::-1]
    print(sum(a[:k]))

=======
Suggestion 3

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    print(sum(a[:k]))

=======
Suggestion 4

def f(n,k,a):
    d={}
    for i in a:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    ans=0
    for i in d:
        if d[i]>=k:
            ans+=k
        else:
            ans+=d[i]
    return ans
n,k=map(int,input().split())
a=list(map(int,input().split()))
print(f(n,k,a))

=======
Suggestion 5

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    if k == 1:
        print(n)
    else:
        ans = 0
        for i in range(n-k+1):
            if a[i+k-1] - a[i] < ans:
                continue
            else:
                ans = a[i+k-1] - a[i]
        print(ans)

=======
Suggestion 6

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    a.reverse()
    #print(a)
    sum = 0
    for i in range(k):
        sum += a[i]
    print(sum)

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a = a[::-1]
    ans = 0
    for i in range(0, n, k):
        ans += 1
    print(ans)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n - 1, n - k - 1, -1):
        ans += a[i]
    print(ans)

=======
Suggestion 9

def solve():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    print(A)
    i = 0
    j = 0
    cnt = 0
    while j < N:
        if A[j] - A[i] >= K:
            i += 1
            cnt += 1
        j += 1
    print(cnt)
solve()

=======
Suggestion 10

def solve(n, k, a):
    a.sort()
    a.reverse()
    sum = 0
    for i in range(k):
        sum += a[i]
    return sum
