Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, y, z, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    ab = []
    for ai in a:
        for bi in b:
            ab.append(ai + bi)

    ab.sort(reverse=True)

    abc = []
    for i in range(min(k, len(ab))):
        for ci in c:
            abc.append(ab[i] + ci)

    abc.sort(reverse=True)

    for i in range(k):
        print(abc[i])

=======
Suggestion 2

def problems123_d():
    pass

=======
Suggestion 3

def main():
    x,y,z,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))
    ab=[i+j for i in a for j in b]
    ab.sort(reverse=True)
    ab=ab[0:k]
    abc=[i+j for i in ab for j in c]
    abc.sort(reverse=True)
    for i in abc[0:k]:
        print(i)

=======
Suggestion 4

def main():
    x, y, z, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    # 从大到小排序
    a.sort(reverse=True)
    b.sort(reverse=True)
    c.sort(reverse=True)

    # 从大到小排序
    ab = []
    for i in range(x):
        for j in range(y):
            ab.append(a[i] + b[j])
    ab.sort(reverse=True)

    # 从大到小排序
    abc = []
    for i in range(min(k, x * y)):
        for j in range(z):
            abc.append(ab[i] + c[j])
    abc.sort(reverse=True)

    # 输出
    for i in range(k):
        print(abc[i])

=======
Suggestion 5

def main():
    X,Y,Z,K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    AB = []
    for a in A:
        for b in B:
            AB.append(a+b)
    AB.sort(reverse=True)

    ABC = []
    for i in range(min(K, len(AB))):
        for c in C:
            ABC.append(AB[i]+c)
    ABC.sort(reverse=True)

    for i in range(K):
        print(ABC[i])

=======
Suggestion 6

def main():
    x,y,z,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))
    a.sort(reverse=True)
    b.sort(reverse=True)
    c.sort(reverse=True)
    sum=[]
    for i in range(x):
        for j in range(y):
            for k in range(z):
                if (i+1)*(j+1)*(k+1)<=k:
                    sum.append(a[i]+b[j]+c[k])
    sum.sort(reverse=True)
    for i in range(k):
        print(sum[i])

=======
Suggestion 7

def main():
    X,Y,Z,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    ans = []
    for i in range(X):
        for j in range(Y):
            for k in range(Z):
                if (i+1)*(j+1)*(k+1) > K:
                    break
                ans.append(A[i]+B[j]+C[k])
    ans.sort(reverse=True)
    for i in range(K):
        print(ans[i])

=======
Suggestion 8

def main():
    x,y,z,k = map(int, input().split())
    a = sorted(list(map(int, input().split())), reverse=True)
    b = sorted(list(map(int, input().split())), reverse=True)
    c = sorted(list(map(int, input().split())), reverse=True)
    ab = []
    for i in range(x):
        for j in range(y):
            ab.append(a[i]+b[j])
    ab.sort(reverse=True)
    abc = []
    for i in range(min(k, x*y)):
        for j in range(z):
            abc.append(ab[i]+c[j])
    abc.sort(reverse=True)
    for i in range(k):
        print(abc[i])

=======
Suggestion 9

def main():
    # 读入数据
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    # 从大到小排序
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)

    # 暴力搜索
    ans = []
    for a in A:
        for b in B:
            for c in C:
                ans.append(a + b + c)

    # 从大到小排序
    ans.sort(reverse=True)

    # 打印前K个
    for i in range(K):
        print(ans[i])

=======
Suggestion 10

def main():
    x,y,z,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))
    a.sort(reverse=True)
    b.sort(reverse=True)
    c.sort(reverse=True)
    ans=[]
    for i in range(x):
        for j in range(y):
            for k in range(z):
                if (i+1)*(j+1)*(k+1)<=k:
                    break
                else:
                    ans.append(a[i]+b[j]+c[k])
    ans.sort(reverse=True)
    for i in range(k):
        print(ans[i])
