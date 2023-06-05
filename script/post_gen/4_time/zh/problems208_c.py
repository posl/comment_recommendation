Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    cnt = k // n
    remain = k % n
    ans = [cnt] * n
    for i in range(remain):
        ans[a[i] - 1] += 1
    for i in range(n):
        print(ans[i])

=======
Suggestion 2

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = [K // N for i in range(N)]
    K %= N
    for i in range(K):
        ans[A[i] - 1] += 1
    for i in range(N):
        print(ans[i])

solve()

=======
Suggestion 3

def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    #print(a)
    #print(n,k)
    #print(a)
    #print("k//n=",k//n)
    #print("k%n=",k%n)
    for i in range(n):
        if k//n>0:
            print(k//n)
        else:
            print(0)


main()

=======
Suggestion 4

def main():
    N,K = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    if K >= N:
        for i in range(N):
            print(K//N)
    else:
        b = []
        for i in range(N):
            b.append([a[i],i])
        b.sort()
        c = K
        for i in range(N):
            if b[i][1] < c:
                print(K//N + 1)
            else:
                print(K//N)
        #print(b)

=======
Suggestion 5

def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    #print(A)
    #print(N,K)
    #print(A[0])
    #print(A[0]-1)
    #print(K//(A[0]-1))
    #print(K//(A[0]-1)+1)
    #print(K//(A[0]-1)+2)
    #print(K//(A[0]-1)+3)
    #print(K//(A[0]-1)+4)
    #print(K//(A[0]-1)+5)
    #print(K//(A[0]-1)+6)
    #print(K//(A[0]-1)+7)
    #print(K//(A[0]-1)+8)
    #print(K//(A[0]-1)+9)
    #print(K//(A[0]-1)+10)
    #print(K//(A[0]-1)+11)
    #print(K//(A[0]-1)+12)
    #print(K//(A[0]-1)+13)
    #print(K//(A[0]-1)+14)
    #print(K//(A[0]-1)+15)
    #print(K//(A[0]-1)+16)
    #print(K//(A[0]-1)+17)
    #print(K//(A[0]-1)+18)
    #print(K//(A[0]-1)+19)
    #print(K//(A[0]-1)+20)
    #print(K//(A[0]-1)+21)
    #print(K//(A[0]-1)+22)
    #print(K//(A[0]-1)+23)
    #print(K//(A[0]-1)+24)
    #print(K//(A[0]-1)+25)
    #print(K//(A[0]-1)+26)
    #print(K//(A[0]-1)+27)
    #print(K//(A[0]-1)+28)
    #print(K//(A[0]-1)+29)
    #print(K//(A[0]-1)+30)
    #print(K//(A[0]-1)+31)
    #print(K//(A[0]-1)+32)
    #print(K//(A[0]-1)+33)
    #print(K//(A[

=======
Suggestion 6

def main():
    N,K = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    n = K//N
    m = K%N
    for i in range(N):
        if a[i] <= n:
            if m > 0:
                print(n+1)
                m -= 1
            else:
                print(n)
        else:
            print(n)

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    if n >= k:
        for i in range(n):
            print(k//n)
    else:
        for i in range(n):
            print(k//n)
        for i in range(k%n):
            print(1)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    n = K // N
    k = K % N
    for i in range(N):
        if i < k:
            print(n+1)
        else:
            print(n)

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = [k // n] * n
    k %= n
    for i in range(k):
        ans[a[i] - 1] += 1
    for i in range(n):
        print(ans[i])

=======
Suggestion 10

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

N, K = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
