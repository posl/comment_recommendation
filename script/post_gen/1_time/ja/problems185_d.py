Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if M == 0:
        print(1)
        return
    if M == N:
        print(0)
        return
    if M == 1:
        print(min(A[0], N - A[0] + 1))
        return
    B = [0] * (M - 1)
    for i in range(M - 1):
        B[i] = A[i + 1] - A[i] - 1
    B.sort()
    print(B[0] + 1)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    if M == 0:
        print(1)
        return
    A.sort()
    A = [0] + A + [N+1]
    d = []
    for i in range(M+1):
        if A[i+1] - A[i] > 1:
            d.append(A[i+1] - A[i] - 1)
    if len(d) == 0:
        print(0)
        return
    k = min(d)
    ans = 0
    for i in range(len(d)):
        ans += (d[i] + k - 1) // k
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    if M == 0:
        print(1)
        return
    A.sort()
    A = [0] + A + [N+1]
    B = []
    for i in range(M+1):
        if A[i+1] - A[i] - 1 > 0:
            B.append(A[i+1] - A[i] - 1)
    if len(B) == 0:
        print(0)
        return
    C = min(B)
    ans = 0
    for i in range(len(B)):
        ans += (B[i] + C - 1) // C
    print(ans)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    if m == 0:
        print(1)
        return
    a.sort()
    a = [0] + a + [n+1]
    b = [a[i+1] - a[i] - 1 for i in range(m+1)]
    b.sort(reverse=True)
    k = 0
    for i in range(m+1):
        if b[i] == 0:
            break
        if k == 0:
            k = b[i]
        else:
            k = gcd(k, b[i])
    print((n - sum(b)) // k + 1)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    if M == 0:
        print(1)
        return
    A.sort()
    B = [A[0] - 1]
    for i in range(1, M):
        B.append(A[i] - A[i - 1] - 1)
    B.append(N - A[M - 1])
    B.sort()
    if B[-1] == 0:
        print(0)
        return
    k = B[-1]
    ans = 1
    for i in range(M):
        ans += (A[i] - 1) // k
        ans += (N - A[i]) // k
    print(ans)
    return

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A + [N+1]
    B = []
    for i in range(M+1):
        B.append(A[i+1] - A[i] - 1)
    B.sort()
    B = B[::-1]
    ans = 0
    for i in range(M+1):
        if i < N % (M+1):
            ans += B[i]//(N//(M+1)+1)
        else:
            ans += B[i]//(N//(M+1))
    print(ans)

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.append(n + 1)
    d = []
    for i in range(m + 1):
        d.append(a[i] - a[i - 1] - 1)
    d.sort()
    d = [i for i in d if i != 0]
    if len(d) == 0:
        print(0)
        return
    k = d[0]
    for i in range(1, len(d)):
        k = gcd(k, d[i])
    print((max(d) - 1) // k + 1)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A + [N+1]
    #print(A)
    B = []
    for i in range(M+1):
        if A[i+1]-A[i]-1 > 0:
            B.append(A[i+1]-A[i]-1)
    #print(B)
    if len(B) == 0:
        print(0)
        exit()
    if len(B) == 1:
        print(1)
        exit()
    C = []
    for i in range(len(B)-1):
        C.append(B[i]+B[i+1])
    #print(C)
    print(min(C))

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.append(n+1)
    a.insert(0,0)

    if m == 0:
        print(1)
        exit()

    if m == n:
        print(0)
        exit()

    l = []
    for i in range(m+1):
        l.append(a[i+1]-a[i]-1)

    k = min(l)
    ans = 0
    for i in l:
        ans += i//k
        if i%k != 0:
            ans += 1

    print(ans)

=======
Suggestion 10

def main():
    N,M=map(int,input().split())
    A=list(map(int,input().split()))

    A.sort()
    A.append(N+1)
    if A[0]!=1:
        A.insert(0,0)
    if A[-1]!=N+1:
        A.append(N+1)
    #print(A)
    B=[]
    for i in range(1,len(A)):
        if A[i]-A[i-1]-1!=0:
            B.append(A[i]-A[i-1]-1)
    B.sort()
    if len(B)==0:
        print(0)
    else:
        k=B[0]
        ans=0
        for i in range(len(B)):
            ans+=B[i]//k
            if B[i]%k!=0:
                ans+=1
        print(ans)
