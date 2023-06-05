Synthesizing 10/10 solutions

=======
Suggestion 1

def get_input():
    n,x,y,z = input().split()
    n = int(n)
    x = int(x)
    y = int(y)
    z = int(z)
    a = input().split()
    b = input().split()
    a = [int(i) for i in a]
    b = [int(i) for i in b]
    return n,x,y,z,a,b

=======
Suggestion 2

def get_input():
    N,X,Y,Z = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    return N,X,Y,Z,A,B

=======
Suggestion 3

def main():
    n, x, y, z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = []
    for i in range(n):
        c.append((a[i] + b[i], a[i], b[i], i + 1))
    c.sort(reverse=True)
    d = []
    for i in range(x):
        d.append(c[i][3])
    d.sort()
    print(*d, sep='\n')
    d = []
    for i in range(x, x + y):
        d.append(c[i][3])
    d.sort()
    print(*d, sep='\n')
    d = []
    for i in range(x + y, x + y + z):
        d.append(c[i][3])
    d.sort()
    print(*d, sep='\n')

=======
Suggestion 4

def main():
    n,x,y,z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = []
    for i in range(n):
        c.append([i+1, a[i], b[i], a[i]+b[i]])
    c.sort(key=lambda x:(x[1], x[0]), reverse=True)
    c = c[:x]
    c.sort(key=lambda x:(x[2], x[0]), reverse=True)
    c = c[:x+y]
    c.sort(key=lambda x:(x[3], x[0]), reverse=True)
    c = c[:x+y+z]
    c.sort(key=lambda x:(x[0]))
    for i in range(x+y+z):
        print(c[i][0])

=======
Suggestion 5

def get_input():
    input_list = []
    while True:
        try:
            input_list.append(input())
        except:
            break
    return input_list

=======
Suggestion 6

def main():
    N,X,Y,Z = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = []
    for i in range(N):
        C.append([i+1,A[i],B[i],A[i]+B[i]])
    C.sort(key=lambda x:(-x[1],-x[2],-x[3]))
    for i in range(X):
        print(C[i][0])
    for i in range(X,X+Y):
        print(C[i][0])
    for i in range(X+Y,X+Y+Z):
        print(C[i][0])

=======
Suggestion 7

def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = []
    for i in range(N):
        C.append((A[i], B[i], i + 1))
    C.sort(key=lambda x: (-x[0], x[2]))
    C = C[:X]
    C.sort(key=lambda x: (-x[1], x[2]))
    C = C[:X + Y]
    C.sort(key=lambda x: (-x[0] - x[1], x[2]))
    C = C[:X + Y + Z]
    C.sort(key=lambda x: x[2])
    for i in range(X + Y + Z):
        print(C[i][2])

=======
Suggestion 8

def get_input():
    inputs = input().split()
    N = int(inputs[0])
    X = int(inputs[1])
    Y = int(inputs[2])
    Z = int(inputs[3])
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    return N, X, Y, Z, A, B

=======
Suggestion 9

def main():
    N,X,Y,Z=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    C=[]
    for i in range(N):
        C.append([i+1,A[i],B[i]])
    C.sort(key=lambda x:(-x[1],x[0]))
    D=C[:X]
    D.sort(key=lambda x:(-x[2],x[0]))
    E=C[X:X+Y]
    E.sort(key=lambda x:(-(x[1]+x[2]),x[0]))
    F=C[X+Y:]
    F.sort(key=lambda x:x[0])
    for i in range(len(D)):
        print(D[i][0])
    for i in range(len(E)):
        print(E[i][0])
    for i in range(len(F)):
        print(F[i][0])
main()

=======
Suggestion 10

def input_data():
    data = []
    for i in range(3):
        data.append(input())
    data.append(input().split())
    data.append(input().split())
    return data
