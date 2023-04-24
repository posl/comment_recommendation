Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = []
    for i in range(1, 2 ** N + 1):
        B.append([i, A[i - 1]])
    while len(B) > 2:
        tmp = []
        for i in range(0, len(B), 2):
            if B[i][1] > B[i + 1][1]:
                tmp.append(B[i])
            else:
                tmp.append(B[i + 1])
        B = tmp
    if B[0][1] > B[1][1]:
        print(B[1][0])
    else:
        print(B[0][0])

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = sorted(A, reverse=True)
    A1 = A[0:2**(N-1)]
    A2 = A[2**(N-1):2**N]
    print(A.index(min(A1, key=lambda x:abs(x-A2[0])))+1)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = A.copy()
    for i in range(N-1):
        for j in range(2**(N-i-1)):
            B[2*j] = max(A[2*j],A[2*j+1])
            B[2*j+1] = min(A[2*j],A[2*j+1])
        A = B.copy()
    print(A.index(min(A))+1)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = sorted(A)
    print(A.index(B[-2])+1)

=======
Suggestion 5

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = a.copy()
    for i in range(1, n):
        c = []
        for j in range(0, 2**(n - i)):
            c.append(max(b[2*j], b[2*j+1]))
        b = c.copy()
    print(a.index(min(b[0], b[1])) + 1)

=======
Suggestion 6

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a = [(x,i) for i,x in enumerate(a)]
    for i in range(n-1):
        b = []
        for j in range(2**(n-i-1)):
            if a[2*j][0] > a[2*j+1][0]:
                b.append(a[2*j])
            else:
                b.append(a[2*j+1])
        a = b
    if a[0][0] > a[1][0]:
        print(a[1][1]+1)
    else:
        print(a[0][1]+1)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    B = sorted(A, reverse=True)
    #print(B)
    C = []
    for i in range(N):
        C.append([B[2**i], 2**i])
        #print(C)
    D = sorted(C, reverse=True)
    #print(D)
    print(D[1][1])

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [(i+1, a) for i,a in enumerate(A)]
    A.sort(key=lambda x: x[1])
    B = [a[0] for a in A]
    while len(B) > 2:
        B = [B[i] for i in range(len(B)) if i%2 == 1]
    print(min(B))

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)
    print(a[-2])

=======
Suggestion 10

def getSecondPlace(n, a):
    #print(n, a)
    first = max(a[0:2**n])
    second = max(a[2**n:])
    return a.index(second) + 1
