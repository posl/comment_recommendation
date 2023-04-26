Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    AB = []
    for i in range(N):
        AB.append([i, A[i], B[i]])

    AB.sort(key=lambda x: x[1], reverse=True)
    AB.sort(key=lambda x: x[2], reverse=True)

    AB = AB[:X + Y + Z]

    AB.sort(key=lambda x: x[0])

    for i in range(X + Y + Z):
        print(AB[i][0] + 1)

=======
Suggestion 2

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    AB = []
    for i in range(N):
        AB.append((A[i], B[i]))

    AB.sort(key=lambda x: x[1], reverse=True)
    AB.sort(key=lambda x: x[0], reverse=True)

    result = []
    for i in range(X):
        result.append(AB[i])

    AB = AB[X:]
    AB.sort(key=lambda x: x[1], reverse=True)

    for i in range(Y):
        result.append(AB[i])

    AB = AB[Y:]
    AB.sort(key=lambda x: x[0] + x[1], reverse=True)

    for i in range(Z):
        result.append(AB[i])

    result.sort(key=lambda x: x[0] + x[1], reverse=True)
    result.sort(key=lambda x: x[1], reverse=True)
    result.sort(key=lambda x: x[0], reverse=True)

    for i in range(len(result)):
        print(A.index(result[i][0]) + 1)

=======
Suggestion 3

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    AB = []
    for i in range(N):
        AB.append([i+1, A[i], B[i]])

    AB = sorted(AB, key=lambda x: x[2], reverse=True)
    AB = sorted(AB, key=lambda x: x[1], reverse=True)

    AB = AB[:X+Y+Z]
    AB = sorted(AB, key=lambda x: x[0])

    for i in range(X+Y+Z):
        print(AB[i][0])

=======
Suggestion 4

def main():
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = []
    for i in range(n):
        c.append([i+1, a[i], b[i], a[i]+b[i]])
    c.sort(key=lambda x: x[3], reverse=True)
    c.sort(key=lambda x: x[2], reverse=True)
    c.sort(key=lambda x: x[1], reverse=True)
    for i in range(x):
        print(c[i][0])
    for i in range(y):
        print(c[i+x][0])
    for i in range(z):
        print(c[i+x+y][0])

=======
Suggestion 5

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = []
    for i in range(N):
        C.append([A[i]+B[i], A[i], B[i], i+1])
    C.sort(reverse=True)
    ans = []
    for i in range(X):
        ans.append(C[i][3])
    for i in range(X, X+Y):
        if C[i][1] > C[i][2]:
            ans.append(C[i][3])
    for i in range(X+Y, X+Y+Z):
        ans.append(C[i][3])
    ans.sort()
    for i in ans:
        print(i)

=======
Suggestion 6

def main():
    n,x,y,z = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = []
    for i in range(n):
        c.append([a[i]+b[i],a[i],b[i],i+1])
    c.sort(key=lambda x:(-x[0],-x[1],-x[2],x[3]))
    for i in range(x+y+z):
        print(c[i][3])

=======
Suggestion 7

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

=======
Suggestion 8

def main():
    n,x,y,z = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = []
    for i in range(n):
        c.append((a[i],b[i],i+1))
    c.sort(key=lambda x: x[2])
    c.sort(key=lambda x: x[1],reverse=True)
    c.sort(key=lambda x: x[0],reverse=True)
    d = c[:x+y+z]
    d.sort(key=lambda x: x[2])
    d.sort(key=lambda x: x[1],reverse=True)
    d.sort(key=lambda x: x[0],reverse=True)
    for i in range(x+y+z):
        print(d[i][2])

=======
Suggestion 9

def get_input_data():
    n,x,y,z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    return n,x,y,z,a,b

=======
Suggestion 10

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 両方とも点数が高い順に並べる
    AB = []
    for i in range(N):
        AB.append({'no': i, 'a': A[i], 'b': B[i]})
    AB.sort(key=lambda x: x['b'], reverse=True)
    AB.sort(key=lambda x: x['a'], reverse=True)

    # 合格者を出力する
    for i in range(X):
        print(AB[i]['no'] + 1)
    for i in range(X, X + Y):
        print(AB[i]['no'] + 1)
    for i in range(X + Y, X + Y + Z):
        print(AB[i]['no'] + 1)
