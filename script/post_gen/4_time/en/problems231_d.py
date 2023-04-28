Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    if A[-1] < B[0]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    print("Yes" if len(set(a)) + len(set(b)) == n + 1 else "No")

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    a.sort()
    b.sort()
    if a[0] > b[m-1]:
        print('No')
    else:
        print('Yes')

=======
Suggestion 4

def solve():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    A.sort()
    B.sort()
    if A[0] == 1 and B[-1] == N:
        print("YES")
    else:
        print("NO")
    return 0

=======
Suggestion 5

def main():
    N,M = map(int,input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i],B[i] = map(int,input().split())
    print(solve(N,M,A,B))

=======
Suggestion 6

def main():
    N,M = map(int,input().split())
    A = []
    B = []
    for i in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    if A[0] == 1 and B[-1] == N:
        print("YES")
    else:
        print("NO")
main()

=======
Suggestion 7

def solve():
    N,M = map(int,input().split())
    A = []
    B = []
    for i in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    if A[0] == 1 and B[0] == N:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')

=======
Suggestion 8

def solve():
    N,M = map(int,input().split())
    A = []
    B = []
    for i in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    if A[0] == 1 and B[-1] == N:
        print("Yes")
    else:
        print("No")
solve()

=======
Suggestion 9

def solve():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(m):
        x,y = map(int,input().split())
        a.append(x)
        b.append(y)
    a.sort()
    b.sort()
    if a[0] == 1 and b[-1] == n:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")

solve()

=======
Suggestion 10

def solve():
    n,m = map(int,input().split())
    if m == 0:
        print('No')
        return
    ab = [list(map(int,input().split())) for _ in range(m)]
    ab.sort()
    if ab[0][0] == 1:
        print('Yes')
        return
    for i in range(m-1):
        if ab[i][0] == ab[i][1]:
            print('No')
            return
        if ab[i][1] == ab[i+1][0]:
            print('Yes')
            return
    print('No')
solve()
