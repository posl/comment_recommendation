Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # 读取数据
    # 读取第一行的n
    line1 = input().split()
    N = int(line1[0])
    M = int(line1[1])
    K = int(line1[2])
    # 读取第二行的数组
    line2 = input().split()
    A = [int(i) for i in line2]
    # 读取第三行的数组
    line3 = input().split()
    B = [int(i) for i in line3]

    # 读取第四行的数组
    line4 = input().split()
    C = [int(i) for i in line4]

    # 读取第五行的数组
    line5 = input().split()
    D = [int(i) for i in line5]
    # 读取第六行的数组
    line6 = input().split()
    E = [int(i) for i in line6]

    # 读取第七行的数组
    line7 = input().split()
    F = [int(i) for i in line7]

    # 读取第八行的数组
    line8 = input().split()
    G = [int(i) for i in line8]

    # 读取第九行的数组
    line9 = input().split()
    H = [int(i) for i in line9]

    # 读取第十行的数组
    line10 = input().split()
    I = [int(i) for i in line10]

    # 读取第十一行的数组
    line11 = input().split()
    J = [int(i) for i in line11]

    # 读取第十二行的数组
    line12 = input().split()
    K = [int(i) for i in line12]

    # 读取第十三行的数组
    line13 = input().split()
    L = [int(i) for i in line13]

    # 读取第十四行的数组
    line14 = input().split()
    M = [int(i) for i in line14]

    # 读取第十五行的数组
    line15 = input().split()

=======
Suggestion 2

def readinput():
    x,y,z,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))
    return x,y,z,k,a,b,c

=======
Suggestion 3

def main():
    x,y,z,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))

    ab = []
    for i in range(x):
        for j in range(y):
            ab.append(a[i]+b[j])

    ab.sort(reverse=True)

    abc = []
    for i in range(min(k,x*y)):
        for j in range(z):
            abc.append(ab[i]+c[j])

    abc.sort(reverse=True)

    for i in range(k):
        print(abc[i])

=======
Suggestion 4

def main():
    x, y, z, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    # a, b, cを大きい順にソート
    a.sort(reverse=True)
    b.sort(reverse=True)
    c.sort(reverse=True)

    # a, b, cの組み合わせを全探索
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
Suggestion 5

def main():
    x,y,z,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))

    ab = []
    for i in range(x):
        for j in range(y):
            ab.append(a[i]+b[j])
    ab.sort(reverse=True)
    ab = ab[:k]

    abc = []
    for i in range(len(ab)):
        for j in range(z):
            abc.append(ab[i]+c[j])
    abc.sort(reverse=True)
    abc = abc[:k]

    for i in range(k):
        print(abc[i])

=======
Suggestion 6

def main():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    AB = []
    for i in range(X):
        for j in range(Y):
            AB.append(A[i] + B[j])
    AB.sort(reverse=True)

    ABC = []
    for i in range(min(K, X * Y)):
        for j in range(Z):
            ABC.append(AB[i] + C[j])
    ABC.sort(reverse=True)

    for i in range(K):
        print(ABC[i])

=======
Suggestion 7

def problems123_d():
    return None

=======
Suggestion 8

def readinput():
    x,y,z,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))
    return x,y,z,k,a,b,c

=======
Suggestion 9

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
