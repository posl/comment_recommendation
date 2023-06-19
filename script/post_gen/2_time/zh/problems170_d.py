Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 1
    for i in range(1, N):
        if A[i] % A[i - 1] != 0:
            ans += 1
    print(ans)

=======
Suggestion 2

def readinput():
    n=int(input())
    a=list(map(int,input().split()))
    return n,a

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    ans = 1
    for i in range(N-1):
        if A[i] != A[i+1]:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        flag = True
        for j in range(N):
            if i != j and A[j] % A[i] == 0:
                flag = False
        if flag:
            ans += 1
    print(ans)

=======
Suggestion 5

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n = int(input())
a = list(map(int, input().split()))

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    B = [0] * (A[-1] + 1)
    for i in range(N):
        if B[A[i]] == 0:
            for j in range(A[i], A[-1] + 1, A[i]):
                B[j] = 1
        else:
            B[A[i]] += 1
    print(N - sum(B))

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if i == 0 or a[i] != a[i-1]:
            ok = True
            for j in range(i+1, n):
                if a[j] % a[i] == 0:
                    ok = False
                    break
            if ok:
                ans += 1
    print(ans)

=======
Suggestion 8

def max_num(a,b):
    if a>b:
        return a
    else:
        return b

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if(A[j]%A[i]==0):
                count += 1
                break
    print(N-count)
