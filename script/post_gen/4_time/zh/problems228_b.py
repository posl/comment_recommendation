Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a-1 for a in A]
    B = [0] * N
    B[X-1] = 1
    for i in range(N):
        if B[i] == 1:
            B[A[i]] = 1
    print(sum(B))

=======
Suggestion 2

def main():
    line1 = input().split()
    line2 = input().split()
    N = int(line1[0])
    X = int(line1[1])
    A = list(map(int,line2))

    #print(N,X,A)

    #A[X-1] = 0
    #print(A)

    #count = 0
    #for i in range(N-1):
    #    if A[i] == i+1:
    #        if A[i+1] == i+2:
    #            count += 1
    #            A[i+1] = 0
    #print(count)

    count = 1
    x = X-1
    while True:
        #print(x)
        if A[x] == 0:
            break
        else:
            count += 1
            x = A[x]-1
    print(count)

=======
Suggestion 3

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a[x-1] = 0
    a = set(a)
    print(len(a))

=======
Suggestion 4

def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    a = [i-1 for i in a]
    f = [0]*n
    f[x-1] = 1
    for i in range(n):
        if f[i] == 1:
            f[a[i]] = 1
    print(sum(f))

=======
Suggestion 5

def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    a[x-1] = 0
    b = [0]*n
    for i in range(n):
        if a[i] != 0:
            b[a[i]-1] += 1
    for i in range(n):
        if b[i] != 0:
            a[i] = 0
    print(sum(a))

=======
Suggestion 6

def main():
    N,X = map(int,input().split())
    A = list(map(int,input().split()))
    #print(N,X,A)
    count = 1
    friend = X
    while True:
        friend = A[friend-1]
        if friend == X:
            break
        count += 1
    print(count)

=======
Suggestion 7

def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    a.insert(0,0)
    b = [0]*(n+1)
    b[x] = 1
    for i in range(1,n+1):
        if b[a[i]] == 1:
            b[i] = 1
    print(sum(b))

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    # print(N, X)
    # print(A)
    B = [0] * N
    B[X - 1] = 1
    # print(B)
    for i in range(N):
        if B[i] == 1:
            B[A[i] - 1] = 1
    print(sum(B))

=======
Suggestion 9

def main():
    n,x = map(int, input().split())
    a = list(map(int, input().split()))
    a[x-1] = 0
    a = [i-1 for i in a]
    #print(a)
    b = [0 for i in range(n)]
    for i in range(n):
        if a[i] != -1:
            b[a[i]] += 1
    #print(b)
    for i in range(n):
        if b[i] != 0:
            b[i] += 1
    #print(b)
    print(sum(b))

=======
Suggestion 10

def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    a[x-1] = 0
    a = sorted(a)
    #print(a)
    for i in range(n):
        if a[i] == 0:
            print(n-i-1)
            break
