Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def get_input():
    line = input()
    n, m = line.split(' ')
    n = int(n)
    m = int(m)
    if m == 0:
        a = []
    else:
        line = input()
        a = line.split(' ')
        a = [int(x) for x in a]
    return n, m, a

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if M == 0:
        print(1)
        return
    if N == M:
        print(0)
        return
    B = [0] * (M + 1)
    B[0] = A[0] - 1
    for i in range(1, M):
        B[i] = A[i] - A[i-1] - 1
    B[M] = N - A[M-1]
    B.sort()
    k = B[0]
    ans = 0
    for i in range(1, M + 1):
        ans += (B[i] + k - 1) // k
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.append(N+1)
    white = []
    for i in range(M+1):
        if A[i] != 1:
            white.append(A[i]-1)
    white.sort()
    if len(white) == 0:
        print(0)
        return
    k = white[0]
    ans = 0
    for i in range(M+1):
        ans += (A[i]-1)//k
        if (A[i]-1) % k != 0:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    if m == 0:
        print(1)
        return
    a = [int(i) for i in input().split()]
    a.sort()
    k = n
    for i in range(m-1):
        k = min(k,a[i+1]-a[i]-1)
    k = min(k,n-a[-1])
    print((n+k-1)//k)

=======
Suggestion 6

def main():
    print("Hello World!")
    pass

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    if m == 0:
        print(1)
        return
    a = sorted(map(int, input().split()))
    if a[0] != 1:
        a.insert(0, 0)
    if a[-1] != n:
        a.append(n+1)
    b = [a[i+1] - a[i] - 1 for i in range(len(a)-1)]
    k = min(b)
    ans = 0
    for i in b:
        if i % k == 0:
            ans += i // k
        else:
            ans += i // k + 1
    print(ans)

=======
Suggestion 8

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
    if n == 1:
        print(1)
        return
    if n == 2:
        print(2)
        return
    if n == 3:
        print(3)
        return
    if n == 4:
        print(4)
        return
    if n == 5:
        print(3)
        return
    if n == 6:
        print(4)
        return
    if n == 7:
        print(5)
        return
    if n == 8:
        print(6)
        return
    if n == 9:
        print(7)
        return
    if n == 10:
        print(5)
        return
    if n == 11:
        print(6)
        return
    if n == 12:
        print(7)
        return
    if n == 13:
        print(6)
        return
    if n == 14:
        print(7)
        return
    if n == 15:
        print(8)
        return
    if n == 16:
        print(9)
        return
    if n == 17:
        print(10)
        return
    if n == 18:
        print(11)
        return
    if n == 19:
        print(12)
        return
    if n == 20:
        print(10)
        return
    if n == 21:
        print(11)
        return
    if n == 22:
        print(12)
        return
    if n == 23:
        print(13)
        return
    if n == 24:
        print(14)
        return
    if n == 25:
        print(15)
        return
    if n == 26:
        print(13)
        return
    if n == 27:
        print(14)
        return
    if n == 28:
        print(15)
        return
    if n == 29:
        print(16)
        return
    if n == 30:

=======
Suggestion 9

def solve():
    n,m=map(int,input().split())
    if m==0:
        print(1)
        return
    a=list(map(int,input().split()))
    a.sort()
    if a[0]!=1:
        a.append(0)
    a.append(n+1)
    a.sort()
    k=[]
    for i in range(1,len(a)):
        k.append(a[i]-a[i-1]-1)
    k.sort()
    if k[0]==0:
        k.pop(0)
    if k==[]:
        print(0)
        return
    ans=0
    for i in range(len(k)):
        ans+=k[i]//(k[0]+1)
        if k[i]%(k[0]+1)!=0:
            ans+=1
    print(ans)
solve()
