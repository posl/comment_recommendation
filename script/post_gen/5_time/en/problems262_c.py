Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(1, n+1):
        if a[i-1] == i:
            cnt += 1
    print(cnt)

=======
Suggestion 2

def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, N+1):
        if a[i-1] == i:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for i in range(N):
        B[A[i]] = i + 1
    ans = 0
    for i in range(1, N + 1):
        if B[i] == i:
            ans += 1
        else:
            if B[B[i]] == i:
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if a[i] < i + 1:
            continue
        else:
            count += a[i] - i - 1
    print(count)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if a[i] > i+1:
            continue
        else:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, n+1):
        if a[i-1] == i: ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = 0
    d = [0]*(n+1)
    for i in range(n):
        d[a[i]] += 1
    for i in range(1,n+1):
        ans += d[i]*(d[i]-1)//2
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    min = 0
    max = 0
    count = 0
    for i in range(N):
        if i+1 == A[i]:
            if min == 0:
                min = i+1
                max = i+1
            else:
                max = i+1
        elif i+1 < A[i]:
            if min == 0:
                min = i+1
                max = A[i]
            else:
                if min <= A[i]:
                    count += 1
                max = A[i]
        else:
            if min == 0:
                min = A[i]
                max = i+1
            else:
                if min <= i+1:
                    count += 1
                max = i+1
    print(count)

=======
Suggestion 9

def sol():
    import sys
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    for i in range(1,n+1):
        if i==a[a[i-1]-1]:
            ans+=1
    print(ans//2)
sol()
