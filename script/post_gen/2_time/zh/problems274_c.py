Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    res = [0] * (2 * n + 1)
    for i in range(n):
        res[a[i]] = i + 1
    for i in range(1, 2 * n + 1):
        print(res[i])

=======
Suggestion 2

def main():
    n=int(input())
    a=list(map(int,input().split()))
    a.insert(0,0)
    b=[0]*(2*n+1)
    for i in range(1,n+1):
        b[i]=1
    for i in range(n,0,-1):
        b[i]=b[i*2]+1
        b[i]=b[i*2+1]+1
    for i in range(1,2*n+1):
        print(b[i])

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0]*(2*N+1)
    for i in range(N):
        B[A[i]] = i+1
    for i in range(1, 2*N+1):
        print(B[i])

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (2 * N + 1)
    for i in range(N):
        B[A[i]] = i + 1
    ans = [0] * (2 * N + 1)
    for i in range(2 * N, 0, -1):
        p = i
        while p <= 2 * N:
            ans[i] += 1
            p += p & -p
        p = B[i]
        while p > 0:
            ans[i] -= 1
            p -= p & -p
    for i in range(2 * N + 1):
        print(ans[i])

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * (2 * N + 1)
    for i in range(N):
        ans[A[i]] = i + 1
    for i in range(1, N + 1):
        j = i
        while j != 1:
            ans[j // 2] = max(ans[j // 2], ans[j] + 1)
            j //= 2
    for i in range(1, 2 * N + 1):
        print(ans[i])

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = [0] * (2 * n + 1)
    for i in range(n):
        d[a[i]] = 1
    for i in range(2 * n, 0, -1):
        d[i // 2] += d[i]
    for i in range(1, 2 * n + 1):
        print(d[i])

main()

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0]*(2*n+1)
    for i in range(n):
        b[a[i]] = i+1
    for i in range(1, 2*n+1):
        j = i
        while True:
            print(b[j])
            if j == 1:
                break
            j = j//2

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (2 * N + 1)
    for i in range(N):
        B[A[i]] = i + 1
    C = [0] * (2 * N + 1)
    for i in range(2 * N, 0, -1):
        p = i
        while p <= 2 * N:
            C[p] += 1
            p += p & -p
        p = B[i]
        while p <= 2 * N:
            C[p] -= 1
            p += p & -p
    for i in range(1, 2 * N + 1):
        print(C[i])

main()

=======
Suggestion 9

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = [0] * (2 * n + 1)
    for i in range(n):
        ans[a[i]] = i + 1
    for i in range(1, 2 * n):
        print(ans[i])

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))

    #生成距离
    d = [0]*(2*N+1)

    #变形虫1与变形虫1是零代的关系。
    d[1] = 0

    #变形虫2与变形虫1有一代之隔。
    d[2] = 1

    #变形虫3与变形虫1相距一代。
    d[3] = 1

    #变形虫4与变形虫2相距一代，与变形虫1相距两代。
    d[4] = 2

    #变形虫5与变形虫2相距一代，与变形虫1相距两代。
    d[5] = 2

    for i in range(1, N):
        #变形虫A_i与变形虫1相距一代。
        d[2*i] = 1
        #变形虫A_i与变形虫1相距一代。
        d[2*i+1] = 1
        #变形虫A_i与变形虫1相距一代。
        d[A[i-1]] = 1

    for i in range(1, N+1):
        for j in range(2*i, 2*N+1, i):
            d[j] = d[i]+1

    for i in range(1, 2*N+1):
        print(d[i])
