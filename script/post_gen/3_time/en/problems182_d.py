Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for i in range(N):
        B[i + 1] = B[i] + A[i]
    B = [0] + B
    B.sort()
    ans = 0
    for i in range(N + 1):
        ans = max(ans, B[i + 1] - B[i])
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i]
        if ans <= 0:
            print(0)
            return
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    for i in range(1, N+1):
        A[i] += A[i-1]
    ans = 0
    for i in range(N+1):
        ans = max(ans, A[i])
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 1:
        print(max(0, A[0]))
        return
    if N == 2:
        print(max(0, A[0]+A[1]))
        return
    if N == 3:
        print(max(0, A[0]+A[1], A[0]+A[1]+A[2]))
        return
    if N == 4:
        print(max(0, A[0]+A[1], A[0]+A[1]+A[2], A[0]+A[1]+A[2]+A[3]))
        return
    if N == 5:
        print(max(0, A[0]+A[1], A[0]+A[1]+A[2], A[0]+A[1]+A[2]+A[3], A[0]+A[1]+A[2]+A[3]+A[4]))
        return
    if N == 6:
        print(max(0, A[0]+A[1], A[0]+A[1]+A[2], A[0]+A[1]+A[2]+A[3], A[0]+A[1]+A[2]+A[3]+A[4], A[0]+A[1]+A[2]+A[3]+A[4]+A[5]))
        return
    if N == 7:
        print(max(0, A[0]+A[1], A[0]+A[1]+A[2], A[0]+A[1]+A[2]+A[3], A[0]+A[1]+A[2]+A[3]+A[4], A[0]+A[1]+A[2]+A[3]+A[4]+A[5], A[0]+A[1]+A[2]+A[3]+A[4]+A[5]+A[6]))
        return
    if N == 8:
        print(max(0, A[0]+A[1], A[0]+A[1]+A[2], A[0]+A[1]+A[2]+A[3], A[0]+A[1]+

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i]
        if ans < 0:
            ans = 0
    print(ans)

=======
Suggestion 6

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    if sum(A) <= 0:
        print(0)
        return
    ans = 0
    for a in A:
        ans += a
        if ans < 0:
            print(0)
            return
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    sum = 0
    for i in range(N):
        ans = max(ans, sum+A[i])
        sum += A[i]
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if sum(A) <= 0:
        print(0)
        return
    else:
        print(sum(A) - min(A))

=======
Suggestion 9

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = 0
    for i in range(n):
        if a[i] <= 0:
            ans += -a[i]
        else:
            ans += a[i]
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    
    #N = 3
    #A = [2, -1, -2]
    
    #N = 5
    #A = [-2, 1, 3, -1, -1]
    
    #N = 5
    #A = [-1000, -1000, -1000, -1000, -1000]
    
    B = [0] * N
    B[0] = A[0]
    for i in range(1, N):
        B[i] = B[i-1] + A[i]
    
    #print(B)
    
    C = [0] * N
    C[0] = B[0]
    for i in range(1, N):
        C[i] = max(C[i-1], B[i])
    
    #print(C)
    
    D = [0] * N
    D[0] = max(0, A[0])
    for i in range(1, N):
        D[i] = max(D[i-1], 0) + A[i]
    
    #print(D)
    
    E = [0] * N
    E[0] = D[0]
    for i in range(1, N):
        E[i] = max(E[i-1], D[i])
    
    #print(E)
    
    ans = 0
    for i in range(N):
        ans = max(ans, C[i], E[i])
    
    print(ans)
