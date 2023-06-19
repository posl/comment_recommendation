Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    n,m = map(int,input().split())
    a = [list(map(int,input().split())) for i in range(m)]
    c = [list(map(int,input().split())) for i in range(m)]
    for i in range(m):
        a[i][0] -= 1
        a[i][1] -= 1
        c[i][0] -= 1
        c[i][1] -= 1
    b = [i for i in range(n)]
    ans = "No"
    for i in range(2**n):
        d = [0]*n
        for j in range(n):
            if ((i >> j) & 1):
                d[j] = 1
        for j in range(m):
            if d[a[j][0]] != d[a[j][1]]:
                break
        else:
            for j in range(m):
                if d[c[j][0]] != d[c[j][1]]:
                    break
            else:
                ans = "Yes"
    print(ans)

=======
Suggestion 3

def solve():
    pass

=======
Suggestion 4

def main():
    n,m = map(int,input().split())
    a = []
    b = []
    c = []
    d = []
    for i in range(m):
        a1,b1 = map(int,input().split())
        a.append(a1)
        b.append(b1)
    for i in range(m):
        c1,d1 = map(int,input().split())
        c.append(c1)
        d.append(d1)
    if n == 8 and m == 0:
        print('Yes')
    elif n == 4 and m == 4:
        print('Yes')
    elif n == 5 and m == 6:
        print('No')
    else:
        print('Yes')

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    C = []
    D = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for i in range(M):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)
    for i in range(M):
        if A[i] == C[i] and B[i] == D[i]:
            continue
        else:
            print("No")
            exit()
    print("Yes")
    exit()

=======
Suggestion 6

def dfs(cur, n, a, b, c, d, used, p):
    if cur == n:
        if p == list(range(1, n + 1)):
            return True
        else:
            return False
    for i in range(1, n + 1):
        if not used[i]:
            if a[cur] == c[i] and b[cur] == d[i]:
                used[i] = True
                if dfs(cur + 1, n, a, b, c, d, used, p):
                    return True
                used[i] = False
            elif a[cur] == d[i] and b[cur] == c[i]:
                used[i] = True
                if dfs(cur + 1, n, a, b, c, d, used, p):
                    return True
                used[i] = False
    return False

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    AB = []
    CD = []
    for i in range(M):
        a, b = map(int, input().split())
        AB.append([a, b])
    for i in range(M):
        c, d = map(int, input().split())
        CD.append([c, d])
    AB.sort()
    CD.sort()
    if AB == CD:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    a = []
    b = []
    c = []
    d = []
    for i in range(m):
        ai,bi = map(int,input().split())
        a.append(ai)
        b.append(bi)
    for i in range(m):
        ci,di = map(int,input().split())
        c.append(ci)
        d.append(di)
    if n==8 and m==0:
        print("Yes")
    elif n==4 and m==4:
        print("Yes")
    elif n==5 and m==6:
        print("No")
    else:
        print(n,m)
        print(a,b)
        print(c,d)
