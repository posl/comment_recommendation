Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,x,y,z = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = []
    for i in range(n):
        c.append([i+1,a[i],b[i],a[i]+b[i]])
    c.sort(key=lambda x:(-x[1],x[0]))
    c = c[:x]
    c.sort(key=lambda x:(-x[2],x[0]))
    c = c[:x+y]
    c.sort(key=lambda x:(-x[3],x[0]))
    c = c[:x+y+z]
    c.sort()
    for i in range(x+y+z):
        print(c[i][0])

=======
Suggestion 2

def main():
    n,x,y,z = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = []
    for i in range(n):
        c.append([i+1,a[i],b[i],a[i]+b[i]])
    c.sort(key=lambda x:(x[1],x[0]),reverse=True)
    c = c[:x]
    c.sort(key=lambda x:(x[2],x[0]),reverse=True)
    c = c[:x+y]
    c.sort(key=lambda x:(x[3],x[0]),reverse=True)
    c = c[:x+y+z]
    c.sort(key=lambda x:x[0])
    for i in range(len(c)):
        print(c[i][0])

=======
Suggestion 3

def main():
    N,X,Y,Z = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = []
    for i in range(N):
        C.append([A[i]+B[i],A[i],B[i],i+1])
    C.sort(reverse=True)
    #print(C)
    ans = []
    for i in range(X):
        ans.append(C[i][3])
    #print(ans)
    C = C[X:]
    C.sort(key=lambda x:(x[1],x[3]),reverse=True)
    #print(C)
    for i in range(Y):
        ans.append(C[i][3])
    #print(ans)
    C = C[Y:]
    C.sort(key=lambda x:(x[0],x[3]),reverse=True)
    #print(C)
    for i in range(Z):
        ans.append(C[i][3])
    #print(ans)
    ans.sort()
    #print(ans)
    for i in range(len(ans)):
        print(ans[i])

main()

=======
Suggestion 4

def get_input():
    input_list = []
    for i in range(17):
        input_list.append(input())
    return input_list

=======
Suggestion 5

def main():
    N,X,Y,Z = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = []
    for i in range(N):
        C.append([i+1,A[i],B[i]])
    C.sort(key=lambda x: x[0])
    C.sort(key=lambda x: x[2],reverse=True)
    C.sort(key=lambda x: x[1],reverse=True)
    for i in range(X):
        print(C[i][0])
    for i in range(X,X+Y):
        print(C[i][0])
    for i in range(X+Y,X+Y+Z):
        print(C[i][0])

=======
Suggestion 6

def get_input():
    #获取输入
    n,x,y,z = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    return n,x,y,z,a,b

=======
Suggestion 7

def input_int():
    return int(input())

=======
Suggestion 8

def main():
    n,x,y,z = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = []
    for i in range(n):
        c.append([a[i]+b[i],a[i],i+1])
    c.sort(reverse=True)
    print(c)
    ans = []
    for i in range(x):
        ans.append(c[i][2])
    for i in range(x,x+y):
        ans.append(c[i][2])
    for i in range(x+y,x+y+z):
        ans.append(c[i][2])
    ans.sort()
    for i in ans:
        print(i)

=======
Suggestion 9

def main():
    n,x,y,z = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = []
    for i in range(n):
        c.append([i+1,a[i],b[i],a[i]+b[i]])
    c.sort(key=lambda x:(-x[1],-x[2],-x[3],x[0]))
    for i in range(x+y+z):
        print(c[i][0])

=======
Suggestion 10

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

    D = []
    for i in range(X):
        D.append(C[i][0])
    for i in range(X, X+Y):
        if C[i][1] == C[X-1][1]:
            D.append(C[i][0])
    for i in range(X+Y, X+Y+Z):
        if C[i][1] == C[X+Y-1][1] and C[i][2] == C[X+Y-1][2]:
            D.append(C[i][0])

    D.sort()
    for i in D:
        print(i)
