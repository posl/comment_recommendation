Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    ans = [0] * N
    ans[0] = 1
    ans[1] = 1
    for i in range(2,N):
        if A[i] == A[i-1]:
            ans[i] = ans[i-1]
        else:
            ans[i] = ans[i-1] + 1
    for i in range(N):
        print(ans[i])

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()
    count = 1
    ans = 0
    for i in range(N-1):
        if A[i] != A[i+1]:
            ans += count*(count-1)//2
            count = 1
        else:
            count += 1
    ans += count*(count-1)//2

    for i in range(N):
        if i == 0:
            print(ans)
        elif A[i-1] != A[i]:
            ans -= count*(count-1)//2
            print(ans)
        else:
            print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    K = [0] * N
    for i in range(N):
        K[i] = A.count(A[i])
    total = sum(K)
    for i in range(N):
        if i == 0:
            print(total - K[i])
        else:
            print(total - K[i] - sum(K[:i]))

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    K = 0
    ans = [0] * N
    for i in range(N):
        if i == 0:
            ans[i] = 1
        elif A[i] != A[i-1]:
            K += 1
            ans[i] = 1
        else:
            ans[i] = ans[i-1] + 1
    for i in range(N):
        print(ans[i])
main()

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    A.sort()
    #print(A)
    K = 0
    for i in range(N):
        if i == 0:
            cnt = 1
        elif A[i] != A[i-1]:
            K += 1
            cnt = 1
        else:
            cnt += 1
        if i == N - 1:
            print(cnt)
        elif A[i] != A[i+1]:
            print(cnt)
    #print(K)
    #for i in range(N):
    #    print(K)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    cnt = 0
    ans = [0] * N
    for i in range(N-1):
        if A[i] == A[i+1]:
            cnt += 1
        else:
            ans[cnt] += 1
            cnt = 0
    ans[cnt] += 1
    for i in range(N):
        print(ans[i])

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    B = [0] * N
    C = [0] * N
    for i in range(N):
        if i == 0:
            B[i] = 1
        else:
            if A[i] != A[i-1]:
                B[i] = 1
    for i in range(N):
        if i == 0:
            C[i] = 1
        else:
            if A[N-i] != A[N-i-1]:
                C[i] = 1
    for i in range(N):
        if i != 0:
            B[i] = B[i] + B[i-1]
            C[i] = C[i] + C[i-1]
    for i in range(N):
        if i == 0:
            print(B[N-1])
        else:
            print(B[N-1]-B[i-1]-C[N-i-1])
main()

=======
Suggestion 9

def main():
    import sys
    readline = sys.stdin.buffer.readline
    mod = 10**9+7
    from collections import Counter

    N = int(readline())
    A = list(map(int,readline().split()))
    c = Counter(A)
    c = sorted(c.items(),key=lambda x:x[0])
    ans = [0]*N
    for i in range(N):
        if c[i][0] > i:
            ans[i] = c[i][1]
    print(*ans,sep='\n')

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = [0]*(n+1)
    ans = 0
    for i in range(n):
        if a[i] != a[i-1]:
            ans += b.count(i)
            b = [0]*(n+1)
        b[a[i]] += 1
    ans += b.count(n)
    b = [0]*(n+1)
    for i in range(n):
        if a[i] != a[i-1]:
            print(ans - b.count(i))
            b = [0]*(n+1)
        b[a[i]] += 1
    print(ans - b.count(n))
