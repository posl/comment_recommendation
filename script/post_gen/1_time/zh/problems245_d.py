Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    b = []
    for i in range(m+1):
        b.append(0)
    for i in range(n+1):
        for j in range(m+1):
            b[j] += a[i] * c[i+j]
    for i in range(m+1):
        print(b[i], end=' ')
    print()

solve()

=======
Suggestion 2

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    c = list(map(int,input().split()))
    b = [0]*(m+1)
    b[m] = c[-1]//a[-1]
    for i in range(m-1,-1,-1):
        b[i] = (c[i]-sum([b[i+j+1]*a[j+1] for j in range(m-i)]))//a[0]
    print(*b)

=======
Suggestion 3

def main():
    pass

=======
Suggestion 4

def solve():
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    C = list(map(int,input().split()))
    B = [0]*(m+1)
    for i in range(n+1):
        B[m] += C[n+m-i]*A[i]
    for i in range(m+1):
        B[i] = (C[i]-B[m])//A[0]
    print(' '.join(map(str,B)))

=======
Suggestion 5

def main():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    c=list(map(int,input().split()))
    b=[0]*(m+1)
    for i in range(m+1):
        b[i]=c[i]-sum([a[j]*b[i-j] for j in range(i)])
    print(*b)

=======
Suggestion 6

def getB(n, m, A, C):
    B = [0 for i in range(m + 1)]
    B[0] = C[0] // A[0]
    for i in range(1, m + 1):
        B[i] = (C[i] - sum([B[j] * A[i - j] for j in range(i)])) // A[0]
    return B

=======
Suggestion 7

def main():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    c=list(map(int,input().split()))
    b=[0]*(m+1)
    b[0]=c[0]/a[0]
    for i in range(1,m+1):
        b[i]=(c[i]-sum([b[j]*a[i-j] for j in range(1,i+1)]))/a[0]
    for i in range(m+1):
        print(int(b[i]),end=' ')

=======
Suggestion 8

def f(x):
    return sum([a[i] * x ** i for i in range(n + 1)])

=======
Suggestion 9

def solve(n,m,a,c):
    b=[0]*(m+1)
    for i in range(m+1):
        b[i]=c[i]
    for i in range(n+1):
        for j in range(m+1):
            b[j]-=a[i]
        for j in range(m,0,-1):
            b[j-1]+=b[j]
    return b
