Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0
    while n > k:
        cnt += 1
        n = n - k + 1
    print(cnt + 1)

=======
Suggestion 2

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    min_num = A[0]
    start = 0
    end = 0
    for i in range(N):
        if min_num > A[i]:
            min_num = A[i]
            start = i
        if min_num == 1:
            end = i
            break
    if end < start + K - 1:
        print(1)
    else:
        print((end - start) // (K - 1) + 1)

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    min_index = a.index(min(a))
    if min_index <= k-1:
        print(1)
    else:
        print((n-2)//(k-1)+1)

=======
Suggestion 4

def solve():
    return

=======
Suggestion 5

def main():
    n,k = input().split()
    n = int(n)
    k = int(k)
    a = input().split()
    a = list(map(int,a))
    cnt = 0
    for i in range(n-k+1):
        cnt += 1
    print(cnt)

=======
Suggestion 6

def main():
    n,k = map(int,input().split())
    A = list(map(int,input().split()))
    min_num = min(A)
    min_index = A.index(min_num)
    if min_index < k:
        if n % (k-1) == 0:
            print(n//(k-1))
        else:
            print(n//(k-1)+1)
    elif min_index >= k:
        if (n-min_index) % (k-1) == 0:
            print((n-min_index)//(k-1))
        else:
            print((n-min_index)//(k-1)+1)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    min = 1000000000
    for i in range(N-K+1):
        if min > A[i+K-1] - A[i]:
            min = A[i+K-1] - A[i]
    print(min)

=======
Suggestion 8

def problem101_c():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    ans=0
    for i in range(n-k):
        if a[i]<a[i+k]:
            ans+=1
    print(ans)

=======
Suggestion 9

def solve(n, k, a):
    ans = 0
    if (n - k) % (k - 1) == 0:
        ans = (n - k) // (k - 1)
    else:
        ans = (n - k) // (k - 1) + 1
    return ans + 1

=======
Suggestion 10

def get_min(a):
    min = a[0]
    for i in range(1, len(a)):
        if a[i] < min:
            min = a[i]
    return min
