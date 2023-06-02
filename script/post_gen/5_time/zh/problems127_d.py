Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    BC = []
    for i in range(M):
        BC.append(list(map(int, input().split())))
    BC.sort(key=lambda x: x[1], reverse=True)
    i = 0
    for j in range(M):
        if BC[j][0] < N:
            for k in range(BC[j][0]):
                if A[i+k] > BC[j][1]:
                    break
                A[i+k] = BC[j][1]
            i += BC[j][0]
        else:
            for k in range(N):
                if A[i+k] > BC[j][1]:
                    break
                A[i+k] = BC[j][1]
            i += N
        if i >= N:
            break
    print(sum(A))

=======
Suggestion 2

def main():
    N,M = input().split()
    N = int(N)
    M = int(M)
    A = input().split()
    A = list(map(int,A))
    B = []
    C = []
    for i in range(M):
        b,c = input().split()
        B.append(int(b))
        C.append(int(c))

    A.sort()
    C.sort(reverse=True)

    for i in range(M):
        if A[N-1] < C[i]:
            A[N-1] = C[i]
            B[i] -= 1
            if B[i] == 0:
                break
            else:
                C[i] = A[N-1]
                C.sort(reverse=True)
        else:
            break

    print(sum(A))

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = []
    c = []
    for i in range(m):
        b_i,c_i = map(int,input().split())
        b.append(b_i)
        c.append(c_i)
    a.sort()
    c.sort(reverse=True)
    ans = 0
    j = 0
    for i in range(n):
        if j < m and c[j] > a[i]:
            ans += c[j]
            j += 1
        else:
            ans += a[i]
    print(ans)

=======
Suggestion 4

def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    b = []
    c = []
    for i in range(m):
        b_i, c_i = map(int, input().split())
        b.append(b_i)
        c.append(c_i)
    b.sort()
    b.reverse()
    c.sort()
    c.reverse()
    sum = 0
    for i in range(n):
        if len(b) == 0:
            break
        if a[i] >= c[0]:
            sum += a[i]
        else:
            sum += c[0]
            b[0] -= 1
            if b[0] == 0:
                b.pop(0)
                c.pop(0)
    print(sum)

main()

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = [0]*m
    c = [0]*m
    for i in range(m):
        b[i],c[i] = map(int,input().split())
    a.sort()
    c.sort()
    ans = 0
    for i in range(n):
        ans += a[i]
    j = n-1
    for i in range(m):
        if a[j] < c[i]:
            ans += c[i]-a[j]
            j -= 1
        else:
            break
    print(ans)

=======
Suggestion 6

def solve(N, M, A, BC):
    A.sort(reverse=True)
    BC.sort(key=lambda x:x[1], reverse=True)
    i = 0
    j = 0
    while i < N and j < M:
        if A[i] < BC[j][1]:
            A[i] = BC[j][1]
            BC[j][0] -= 1
            if BC[j][0] == 0:
                j += 1
        else:
            break
        i += 1
    return sum(A)

=======
Suggestion 7

def problems127_d():
    pass

=======
Suggestion 8

def solve(n, m, a, b, c):
    if n == 0 or m == 0:
        return 0
    a.sort(reverse=True)
    b.sort(reverse=True)
    c.sort(reverse=True)
    i = 0
    j = 0
    k = 0
    ans = 0
    while i < n and j < m:
        if a[i] >= c[k]:
            ans += a[i]
            i += 1
        else:
            ans += c[k]
            k += 1
            j += 1
    while i < n:
        ans += a[i]
        i += 1
    return ans

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = []
    c = []
    for i in range(m):
        x,y = map(int,input().split())
        b.append(x)
        c.append(y)
    sum = 0
    for i in range(n):
        sum += a[i]
    for i in range(m):
        sum += (c[i]-a[b[i]-1])
    print(sum)

main()

=======
Suggestion 10

def max_card(n, m, a, b, c):
    a.sort(reverse=True)
    sum = 0
    for i in range(m):
        if b[i] >= n:
            sum += c[i] * n
            return sum
        else:
            sum += c[i] * b[i]
            n -= b[i]
    sum += a[0] * n
    return sum
