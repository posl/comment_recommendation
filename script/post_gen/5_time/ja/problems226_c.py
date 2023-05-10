Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    T = [0] * N
    K = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], K[i], *A[i] = map(int, input().split())

    ans = 0
    for i in range(N-1, -1, -1):
        if K[i] == 0:
            ans = max(ans, T[i])
        else:
            K[i] -= 1
            T[i] += T[A[i][0]-1]
            for j in range(1, len(A[i])):
                K[A[i][j]-1] -= 1
    print(ans)

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def main():
    N = int(input())
    T = [0]*(N+1)
    K = [0]*(N+1)
    A = [0]*(N+1)
    for i in range(1,N+1):
        T[i],K[i] = map(int,input().split())
        A[i] = list(map(int,input().split()))
    dp = [0]*(N+1)
    for i in range(1,N+1):
        for j in range(K[i]):
            dp[i] = max(dp[i],dp[A[i][j]]+T[i])
    print(max(dp))
main()

=======
Suggestion 4

def main():
    N = int(input())
    T = []
    A = []
    for i in range(N):
        t, k, *a = map(int, input().split())
        T.append(t)
        A.append(a)
    print(T)
    print(A)

=======
Suggestion 5

def get_ints(): return map(int, input().split())

=======
Suggestion 6

def readinput():
    n=int(input())
    t=[]
    a=[]
    for _ in range(n):
        line=input().split()
        t.append(int(line[0]))
        a.append([int(line[2+i])-1 for i in range(int(line[1]))])
    return n,t,a

=======
Suggestion 7

def get_input():
    n = int(input())
    t = [0] * n
    k = [0] * n
    a = [0] * n
    for i in range(n):
        t[i], k[i] = map(int, input().split())
        a[i] = list(map(int, input().split()))
    return n, t, k, a

=======
Suggestion 8

def main():
    return 0

=======
Suggestion 9

def solve():
    pass
