Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,m = map(int,input().split())
    if m == 0:
        print(1)
        return
    a = list(map(int,input().split()))
    a.sort()
    if a[0] != 1:
        a.insert(0,0)
    if a[-1] != n:
        a.append(n+1)
    k = n
    for i in range(len(a)-1):
        if a[i+1] - a[i] - 1 > 0:
            k = min(k,a[i+1] - a[i] - 1)
    ans = 0
    for i in range(len(a)-1):
        ans += (a[i+1] - a[i] - 1) // k
        if (a[i+1] - a[i] - 1) % k != 0:
            ans += 1
    print(ans)
    return

=======
Suggestion 2

def main():
    n,m=map(int,input().split())
    if m==0:
        print(1)
        return
    mlist=list(map(int,input().split()))
    mlist.sort()
    klist=[]
    for i in range(m-1):
        klist.append(mlist[i+1]-mlist[i])
    klist.sort()
    k=klist[0]
    count=0
    for i in range(m):
        count+=((mlist[i]-1)//k)
        if (mlist[i]-1)%k!=0:
            count+=1
    count+=((n-mlist[m-1])//k)
    if (n-mlist[m-1])%k!=0:
        count+=1
    print(count)
    return

main()

=======
Suggestion 3

def main():
    N, M = [int(x) for x in input().split()]
    if M == 0:
        print(1)
        return
    A = [int(x) for x in input().split()]
    A.sort()
    if A[0] != 1:
        A = [0] + A
    if A[-1] != N:
        A = A + [N+1]
    #print(A)
    k = 1
    while True:
        for i in range(0, len(A)-1):
            if A[i+1] - A[i] - 1 < k:
                break
        else:
            print(k)
            return
        k += 1

main()

=======
Suggestion 4

def solve(n, m, a):
    if m == 0:
        return 1
    a.sort()
    a.append(n + 1)
    k = 1
    b = []
    for i in range(m):
        if a[i + 1] - a[i] - 1 > 0:
            b.append(a[i + 1] - a[i] - 1)
    return (max(b) + k - 1) // k

=======
Suggestion 5

def solution():
    return

=======
Suggestion 6

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
        print(0)
        return
    if n == 2:
        if m == 1:
            print(1)
        else:
            print(0)
        return
    if n == 3:
        if m == 2:
            print(0)
        elif m == 1:
            if a[0] == 1 or a[0] == 3:
                print(1)
            else:
                print(0)
        else:
            print(0)
        return
    if n == 4:
        if m == 3:
            print(0)
        elif m == 2:
            if a[0] == 1 and a[1] == 2:
                print(0)
            else:
                print(1)
        elif m == 1:
            if a[0] == 1 or a[0] == 4:
                print(1)
            else:
                print(0)
        else:
            print(0)
        return
    if n == 5:
        if m == 4:
            print(0)
        elif m == 3:
            if a[0] == 1 and a[1] == 3 and a[2] == 5:
                print(0)
            else:
                print(1)
        elif m == 2:
            if a[0] == 1 and a[1] == 3:
                print(1)
            elif a[0] == 2 and a[1] == 4:
                print(1)
            else:
                print(0)
        elif m == 1:
            if a[0] == 1 or a[0] == 4:
                print(1)
            else:
                print(0)
        else:
            print(0)
        return
    if m == 0:
        print(1)
        return
    if m == 1:
        if a[0] == 1 or a[0] == n:
            print(1)
        else:

=======
Suggestion 7

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.append(N+1)
    if M == 0:
        print(1)
        return
    if N == M:
        print(0)
        return
    if M == 1:
        print(N-1)
        return
    B = []
    for i in range(M):
        if A[i+1]-A[i]-1 > 0:
            B.append(A[i+1]-A[i]-1)
    B.sort()
    k = B[0]
    ans = 0
    for i in B:
        ans += (i+k-1)//k
    print(ans)

solve()

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    if m == 0:
        print(1)
        return
    a = list(map(int, input().split()))
    a.sort()
    if a[0] != 1:
        a.append(0)
    a.append(n+1)
    a.sort()
    b = []
    for i in range(1, m+2):
        if a[i] - a[i-1] - 1 > 0:
            b.append(a[i] - a[i-1] - 1)
    k = min(b)
    ans = 0
    for i in range(len(b)):
        ans += (b[i] + k - 1) // k
    print(ans)

=======
Suggestion 9

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    if M == 0:
        print(1)
        exit()
    if N == M:
        print(0)
        exit()
    B = []
    for i in range(1,M):
        B.append(A[i]-A[i-1]-1)
    B.sort()
    print(sum(B[0:N-M]))

=======
Suggestion 10

def solve(n, m, a):
    if m == 0:
        return 1
    a.sort()
    a.append(n+1)
    s = []
    for i in range(m+1):
        if a[i+1] - a[i] > 1:
            s.append(a[i+1] - a[i] - 1)
    if len(s) == 0:
        return 0
    k = min(s)
    ans = 0
    for i in range(len(s)):
        ans += (s[i] + k - 1) // k
    return ans

n, m = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, m, a))
