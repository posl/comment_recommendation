Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N - 1):
        if A[i] != A[i + 1]:
            ans += N - i - 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    ans = 0
    for i in range(1,N):
        if A[i-1] != A[i]:
            ans += i
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if a[i] != a[j]:
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n-1):
        ans += n - (i + 1) - (a[i] == a[i+1])
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n-1):
        ans += n - 1 - bisect.bisect_left(a, a[i], i+1)
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-1):
        ans += (N-1-i)
    for i in range(N-1):
        if A[i] == A[i+1]:
            ans -= (N-1-i-1)
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int,input().split()))
    s = set(a)
    print(len(s)*(len(s)-1)//2)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print((N - 1) * N // 2 - (N - len(set(A))))

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))

    A = sorted(A)
    #print(A)

    ans = 0
    for i in range(N):
        if i == 0:
            if A[i] != A[i+1]:
                ans += 1
        elif i == N-1:
            if A[i] != A[i-1]:
                ans += 1
        else:
            if A[i] != A[i-1] and A[i] != A[i+1]:
                ans += 1
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(A)
    A.sort()
    #print(A)
    #print(len(A))
    sum = 0
    for i in range(len(A)-1):
        sum += i+1
    print(sum)
