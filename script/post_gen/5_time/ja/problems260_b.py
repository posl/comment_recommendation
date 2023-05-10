Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = []
    for i in range(N):
        C.append([i+1, A[i], B[i], A[i]+B[i]])
    C.sort(key=lambda x: x[3], reverse=True)
    C.sort(key=lambda x: x[2], reverse=True)
    C.sort(key=lambda x: x[1], reverse=True)
    ans = []
    for i in range(X):
        ans.append(C[i][0])
    for i in range(X, X+Y):
        ans.append(C[i][0])
    for i in range(X+Y, X+Y+Z):
        ans.append(C[i][0])
    ans.sort()
    for i in range(len(ans)):
        print(ans[i])

=======
Suggestion 2

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    AB = []
    for i in range(N):
        AB.append([i, A[i] + B[i]])
    AB.sort(key=lambda x: x[0])
    AB.sort(key=lambda x: x[1], reverse=True)
    AB = AB[:X+Y+Z]
    AB.sort(key=lambda x: x[0])
    AB.sort(key=lambda x: x[1], reverse=True)
    AB = AB[:X+Y]
    AB.sort(key=lambda x: x[0])
    AB.sort(key=lambda x: x[1], reverse=True)
    AB = AB[:X]
    AB.sort(key=lambda x: x[0])
    AB.sort(key=lambda x: x[1], reverse=True)
    for i in range(X):
        print(AB[i][0] + 1)

=======
Suggestion 3

def solve():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    AB = []
    for i in range(N):
        AB.append((A[i], B[i], i+1))
    AB.sort(key=lambda x: x[2])
    AB.sort(key=lambda x: x[1], reverse=True)
    AB.sort(key=lambda x: x[0], reverse=True)
    AB = AB[:X+Y+Z]
    AB.sort(key=lambda x: x[2])
    AB.sort(key=lambda x: x[1], reverse=True)
    AB.sort(key=lambda x: x[0], reverse=True)
    for a, b, i in AB:
        print(i)

=======
Suggestion 4

def main():
    n,x,y,z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = []
    for i in range(n):
        c.append([i+1,a[i],b[i],a[i]+b[i]])
    c.sort(key=lambda x:(-x[3],x[0]))
    for i in range(x):
        print(c[i][0])
    for i in range(x,x+y):
        print(c[i][0])
    for i in range(x+y,x+y+z):
        print(c[i][0])

=======
Suggestion 5

def main():
    n,x,y,z = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = []
    for i in range(n):
        c.append([a[i]+b[i],a[i],b[i],i+1])
    c.sort(reverse=True)
    d = []
    for i in range(x):
        d.append([c[i][1]+c[i][2],c[i][1],c[i][2],c[i][3]])
    d.sort(reverse=True)
    e = []
    for i in range(y):
        e.append([c[i+x][2],c[i+x][1],c[i+x][2],c[i+x][3]])
    e.sort(reverse=True)
    f = []
    for i in range(z):
        f.append([c[i+x+y][0],c[i+x+y][1],c[i+x+y][2],c[i+x+y][3]])
    f.sort(reverse=True)
    g = []
    for i in range(x+y+z):
        g.append([c[i][3]])
    for i in range(x):
        g[d[i][0]-1].append(d[i][3])
    for i in range(y):
        g[e[i][0]-1].append(e[i][3])
    for i in range(z):
        g[f[i][0]-1].append(f[i][3])
    g.sort()
    for i in range(n):
        if len(g[i]) > 1:
            for j in range(len(g[i])-1):
                print(g[i][j+1])
        else:
            print(g[i][0])

=======
Suggestion 6

def main():
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = []
    for i in range(n):
        c.append((a[i], b[i], i + 1))
    c.sort(key=lambda x: x[2])
    c.sort(key=lambda x: x[1], reverse=True)
    c.sort(key=lambda x: x[0], reverse=True)
    for i in range(x):
        print(c[i][2])
    for i in range(y):
        print(c[i + x][2])
    for i in range(z):
        print(c[i + x + y][2])

=======
Suggestion 7

def main():
    n,x,y,z = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = []
    for i in range(n):
        c.append([a[i]+b[i],a[i],b[i],i+1])
    c.sort(reverse=True)
    ans = []
    for i in range(x):
        ans.append(c[i][3])
    for i in range(x,x+y):
        if c[i][1] > c[i][2]:
            ans.append(c[i][3])
    for i in range(x+y,x+y+z):
        ans.append(c[i][3])
    ans.sort()
    for i in range(len(ans)):
        print(ans[i])

=======
Suggestion 8

def main():
    n,x,y,z = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = [[i+1,a[i],b[i],a[i]+b[i]] for i in range(n)]
    c.sort(key=lambda x:(-x[1],x[0]))
    c = c[:x]
    c.sort(key=lambda x:(-x[2],x[0]))
    c = c[:x+y]
    c.sort(key=lambda x:(-x[3],x[0]))
    c = c[:x+y+z]
    c.sort(key=lambda x:x[0])
    for i in range(x+y+z):
        print(c[i][0])

=======
Suggestion 9

def main():
    N,X,Y,Z = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = []
    for i in range(N):
        C.append([i+1,A[i],B[i],A[i]+B[i]])
    C.sort(key=lambda x:(-x[1],-x[2],-x[3],x[0]))
    for i in range(X):
        print(C[i][0])
    for i in range(X,X+Y):
        print(C[i][0])
    for i in range(X+Y,X+Y+Z):
        print(C[i][0])
main()

=======
Suggestion 10

def main():
    n,x,y,z = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = []
    for i in range(n):
        c.append([i+1,a[i],b[i]])
    c.sort(key=lambda x:(-x[1],x[0]))
    c.sort(key=lambda x:(-x[2],x[0]))
    c.sort(key=lambda x:(-x[1]-x[2],x[0]))
    for i in range(x+y+z):
        print(c[i][0])
