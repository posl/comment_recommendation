Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                for l in range(k+1, N):
                    ans = max(ans, A[i]*P + A[j]*Q + A[k]*R + A[l])
    print(ans)

=======
Suggestion 2

def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for x in range(N-3):
        for y in range(x+1, N-2):
            for z in range(y+1, N-1):
                for w in range(z+1, N):
                    ans = max(ans, P*A[x]+Q*A[y]+R*A[z]+A[w])
    print(ans)

=======
Suggestion 3

def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                for l in range(k+1, N):
                    ans = max(ans, A[i]*P + A[j]*Q + A[k]*R + A[l]*(0))
    if ans == 0:
        print("No")
    else:
        print("Yes")

=======
Suggestion 4

def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for x in range(N):
        for y in range(x+1, N):
            for z in range(y+1, N):
                for w in range(z+1, N):
                    if A[x] + A[y] + A[z] + A[w] == P + Q + R:
                        ans = 1
                        break
    if ans == 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N-4):
        for j in range(i+1,N-3):
            for k in range(j+1,N-2):
                for l in range(k+1,N-1):
                    ans = max(ans, P*A[i] + Q*A[j] + R*A[k] + A[l])
    print(ans)

=======
Suggestion 6

def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))

    #A_x + A_{x+1} + ... + A_{y-1} = P
    #A_y + A_{y+1} + ... + A_{z-1} = Q
    #A_z + A_{z+1} + ... + A_{w-1} = R

    #x < y < z < w
    #A_x + A_{x+1} + ... + A_{y-1} = P
    #A_y + A_{y+1} + ... + A_{z-1} = Q
    #A_z + A_{z+1} + ... + A_{w-1} = R
    #A_x + A_{x+1} + ... + A_{y-1} + A_y + A_{y+1} + ... + A_{z-1} + A_z + A_{z+1} + ... + A_{w-1} = P + Q + R

    #A_x + A_{x+1} + ... + A_{y-1} + A_y + A_{y+1} + ... + A_{z-1} = P + Q
    #A_z + A_{z+1} + ... + A_{w-1} = R
    #A_x + A_{x+1} + ... + A_{y-1} + A_y + A_{y+1} + ... + A_{z-1} + A_z + A_{z+1} + ... + A_{w-1} = P + Q + R
    #A_x + A_{x+1} + ... + A_{y-1} + A_y + A_{y+1} + ... + A_{z-1} + A_z + A_{z+1} + ... + A_{w-1} = P + Q + R
    #A_x + A_{x+1} + ... + A_{y-1} + A_y + A_{y+1} + ... + A_{z-1} = P + Q
    #A_x + A_{x+1} + ... + A_{y

=======
Suggestion 7

def main():
    #input
    N,P,Q,R=map(int,input().split())
    A=list(map(int,input().split()))
    #solve
    ans="No"
    for i in range(N-3):
        for j in range(i+1,N-2):
            for k in range(j+1,N-1):
                if P*A[i]+Q*A[j]+R*A[k]==P*max(A[:i])+Q*max(A[i:j])+R*max(A[j:k]):
                    ans="Yes"
                    break
    #output
    print(ans)

=======
Suggestion 8

def main():
    import sys
    input=sys.stdin.readline
    #functions
    def solve():
        for i in range(1,n):
            a[i]+=a[i-1]
        for i in range(1,n):
            b[i]=a[i-1]
        for i in range(1,n):
            c[i]=a[i-1]
        for i in range(1,n):
            d[i]=a[i-1]
        for i in range(1,n):
            if b[i-1]+p==b[i]:
                b[i]=b[i-1]
            else:
                b[i]=min(b[i-1],b[i])
        for i in range(1,n):
            if c[i-1]+q==c[i]:
                c[i]=c[i-1]
            else:
                c[i]=min(c[i-1],c[i])
        for i in range(1,n):
            if d[i-1]+r==d[i]:
                d[i]=d[i-1]
            else:
                d[i]=min(d[i-1],d[i])
        for i in range(1,n):
            if b[i-1]+p==b[i] and c[i-1]+q==c[i] and d[i-1]+r==d[i]:
                return "Yes"
        return "No"
    #inputs
    n,p,q,r=map(int,input().split())
    a=list(map(int,input().split()))
    b=[0]*n
    c=[0]*n
    d=[0]*n
    #solve
    print(solve())

=======
Suggestion 9

def solve(N,P,Q,R,A):
    # write your code here
    pass

=======
Suggestion 10

def read_int():
    return int(input())
