Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if a[i] != a[j] and a[j] != a[k] and a[k] != a[i]:
                    if a[i] + a[j] > a[k] and a[j] + a[k] > a[i] and a[k] + a[i] > a[j]:
                        ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    ans = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                if A[i] != A[j] and A[j] != A[k] and A[k] != A[i]:
                    ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if a[i] != a[j] != a[k] != a[i]:
                    ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N=int(input())
    A=list(map(int,input().split()))
    A.sort()
    ans=0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if A[i]!=A[j] and A[j]!=A[k] and A[k]!=A[i]:
                    if A[i]+A[j]>A[k]:
                        ans+=1
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    c = [0] * (2 * 10 ** 5 + 1)
    for i in range(n):
        c[a[i]] += 1
    ans = 0
    for i in range(n):
        c[a[i]] -= 1
        for j in range(i + 1, n):
            c[a[j]] -= 1
            if c[a[i]] > 0:
                ans += c[a[i]]
            if c[a[j]] > 0:
                ans += c[a[j]]
            c[a[j]] += 1
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if A[i] != A[j] and A[j] != A[k] and A[k] != A[i] and A[i]+A[j] > A[k]:
                    ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if a[i] != a[j] and a[j] != a[k] and a[k] != a[i] and a[i] + a[j] > a[k]:
                    ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A)

=======
Suggestion 9

def main():
    N = int(input())
    A = input().split()
    A = list(map(int, A))
    A.sort()
    count = 0
    for i in range(N):
        if i == 0:
            if A[i] != A[i+1]:
                count += 1
        elif i == N-1:
            if A[i] != A[i-1]:
                count += 1
        else:
            if A[i] != A[i-1] and A[i] != A[i+1]:
                count += 1
    print(count)
