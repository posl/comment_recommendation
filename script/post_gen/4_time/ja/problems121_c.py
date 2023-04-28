Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #print(M)
    result = 0
    for i in range(N):
        if M > 0:
            if M >= B[i]:
                result += A[i] * B[i]
                M -= B[i]
            else:
                result += A[i] * M
                M = 0
        else:
            break
    print(result)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    drinks = []
    for _ in range(n):
        a, b = map(int, input().split())
        drinks.append((a, b))
    drinks.sort()
    ans = 0
    for a, b in drinks:
        if m >= b:
            ans += a * b
            m -= b
        else:
            ans += a * m
            break
    print(ans)

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        ai,bi = map(int,input().split())
        a.append(ai)
        b.append(bi)
    ans = 0
    for i in range(n):
        if m > 0:
            if b[i] <= m:
                ans += a[i]*b[i]
                m -= b[i]
            else:
                ans += a[i]*m
                m = 0
        else:
            break
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    ans = 0
    for a, b in AB:
        if M == 0:
            break
        if b <= M:
            ans += a * b
            M -= b
        else:
            ans += a * M
            M = 0
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    AB = []
    for i in range(N):
        A, B = map(int, input().split())
        AB.append([A, B])
    AB.sort()
    ans = 0
    for i in range(N):
        if M >= AB[i][1]:
            ans += AB[i][0] * AB[i][1]
            M -= AB[i][1]
        else:
            ans += AB[i][0] * M
            break
    print(ans)

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int,input().split())
    ans = 0
    #print(a)
    #print(b)
    for i in range(n):
        if m <= b[i]:
            ans += a[i] * m
            break
        else:
            ans += a[i] * b[i]
            m -= b[i]
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()

    ans = 0
    for i in range(N):
        if M <= AB[i][1]:
            ans += M * AB[i][0]
            break
        else:
            ans += AB[i][0] * AB[i][1]
            M -= AB[i][1]

    print(ans)

=======
Suggestion 8

def main():
    N,M = map(int,input().split())
    AB = []
    for i in range(N):
        AB.append(list(map(int,input().split())))
    AB.sort()
    ans = 0
    for i in range(N):
        if M == 0:
            break
        if M <= AB[i][1]:
            ans += M*AB[i][0]
            M = 0
        else:
            ans += AB[i][0]*AB[i][1]
            M -= AB[i][1]
    print(ans)

=======
Suggestion 9

def solve():
    #input
    N,M = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a,b = map(int, input().split())
        A.append(a)
        B.append(b)
    #calculate
    #Aの値が小さい順に並べる
    A,B = zip(*sorted(zip(A,B)))
    #print(A,B)
    ans = 0
    for i in range(N):
        if B[i] >= M:
            ans += A[i] * M
            break
        else:
            ans += A[i] * B[i]
            M -= B[i]
    #output
    print(ans)

=======
Suggestion 10

def solve():
    N,M = map(int,input().split())
    AB = [list(map(int,input().split())) for _ in range(N)]
    AB.sort()
    ans = 0
    for i in range(N):
        if M > AB[i][1]:
            M -= AB[i][1]
            ans += AB[i][0]*AB[i][1]
        else:
            ans += AB[i][0]*M
            break
    print(ans)
