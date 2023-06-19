Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, y, z, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    a.sort(reverse=True)
    b.sort(reverse=True)
    c.sort(reverse=True)

    ab = []
    for i in range(x):
        for j in range(y):
            ab.append(a[i] + b[j])
    ab.sort(reverse=True)

    abc = []
    for i in range(min(k, len(ab))):
        for j in range(z):
            abc.append(ab[i] + c[j])
    abc.sort(reverse=True)

    for i in range(k):
        print(abc[i])

=======
Suggestion 2

def main():
    X,Y,Z,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    #print(A)
    #print(B)
    #print(C)
    AB = []
    for i in range(X):
        for j in range(Y):
            AB.append(A[i]+B[j])
    #print(AB)
    AB.sort(reverse=True)
    #print(AB)
    ABC = []
    for i in range(min(K,X*Y)):
        for j in range(Z):
            ABC.append(AB[i]+C[j])
    #print(ABC)
    ABC.sort(reverse=True)
    for i in range(K):
        print(ABC[i])

=======
Suggestion 3

def main():
    x, y, z, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    ab = [i + j for i in a for j in b]
    ab.sort(reverse=True)
    ab = ab[:k]

    abc = [i + j for i in ab for j in c]
    abc.sort(reverse=True)
    for i in abc[:k]:
        print(i)

=======
Suggestion 4

def main():
    #输入
    X,Y,Z,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    #解法
    AB = []
    for a in A:
        for b in B:
            AB.append(a+b)
    AB.sort(reverse=True)
    ABC = []
    for i in range(min(K,len(AB))):
        for c in C:
            ABC.append(AB[i]+c)
    ABC.sort(reverse=True)
    #输出
    for i in range(K):
        print(ABC[i])

=======
Suggestion 5

def main():
    x,y,z,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))
    a.sort(reverse=True)
    b.sort(reverse=True)
    c.sort(reverse=True)
    ab=[]
    for i in range(x):
        for j in range(y):
            ab.append(a[i]+b[j])
    ab.sort(reverse=True)
    abc=[]
    for i in range(min(k,x*y)):
        for j in range(z):
            abc.append(ab[i]+c[j])
    abc.sort(reverse=True)
    for i in range(k):
        print(abc[i])

=======
Suggestion 6

def main():
    # 读取输入
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    # 从大到小排序
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)

    # 三重循环
    ans = []
    for a in A:
        for b in B:
            for c in C:
                ans.append(a + b + c)

    # 从大到小排序
    ans.sort(reverse=True)

    # 输出答案
    for i in range(K):
        print(ans[i])

main()

=======
Suggestion 7

def main():
    x,y,z,k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    ab = []
    for i in range(x):
        for j in range(y):
            ab.append(a[i] + b[j])

    ab.sort()
    c.sort(reverse=True)

    abc = []
    for i in range(min(k, x * y)):
        for j in range(z):
            abc.append(ab[i] + c[j])

    abc.sort(reverse=True)

    for i in range(k):
        print(abc[i])

=======
Suggestion 8

def main():
    x,y,z,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))

    a.sort(reverse=True)
    b.sort(reverse=True)
    c.sort(reverse=True)

    ab = []
    for aa in a:
        for bb in b:
            ab.append(aa+bb)

    ab.sort(reverse=True)

    abc = []
    for i in range(k):
        for cc in c:
            abc.append(ab[i]+cc)

    abc.sort(reverse=True)
    for i in range(k):
        print(abc[i])

=======
Suggestion 9

def main():
    X,Y,Z,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    ans = []
    for a in A:
        for b in B:
            for c in C:
                ans.append(a+b+c)
    ans.sort(reverse=True)
    for i in range(K):
        print(ans[i])

=======
Suggestion 10

def main():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    AB = []
    for a in A:
        for b in B:
            AB.append(a + b)
    AB.sort(reverse=True)

    ABC = []
    for i in range(min(K, len(AB))):
        for c in C:
            ABC.append(AB[i] + c)
    ABC.sort(reverse=True)

    for i in range(K):
        print(ABC[i])
