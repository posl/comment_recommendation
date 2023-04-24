Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
    for ab in AB[:K]:
        for c in C:
            ABC.append(ab + c)
    ABC.sort(reverse=True)
    for i in range(K):
        print(ABC[i])

=======
Suggestion 2

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
    for c in C:
        for ab in AB[:K]:
            ABC.append(ab + c)
    ABC.sort(reverse=True)
    for i in range(K):
        print(ABC[i])

=======
Suggestion 3

def main():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    L = []
    for i in range(X):
        for j in range(Y):
            L.append(A[i] + B[j])
    L.sort(reverse=True)
    M = []
    for i in range(min(K, X * Y)):
        for j in range(Z):
            M.append(L[i] + C[j])
    M.sort(reverse=True)
    for i in range(K):
        print(M[i])

=======
Suggestion 4

def main():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    AB = []
    for a in A:
        for b in B:
            AB.append(a + b)
    AB.sort(reverse=True)
    ABC = []
    for ab in AB[:K]:
        for c in C:
            ABC.append(ab + c)
    ABC.sort(reverse=True)
    for i in range(K):
        print(ABC[i])

=======
Suggestion 5

def main():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    
    AB = []
    for a in A:
        for b in B:
            AB.append(a + b)
    AB.sort(reverse = True)
    AB = AB[:K]
    
    ABC = []
    for ab in AB:
        for c in C:
            ABC.append(ab + c)
    ABC.sort(reverse = True)
    ABC = ABC[:K]
    
    for abc in ABC:
        print(abc)

=======
Suggestion 6

def main():
    x, y, z, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    ab = []
    for i in range(x):
        for j in range(y):
            ab.append(a[i] + b[j])
    ab.sort(reverse=True)

    abc = []
    for i in range(min(k, x * y)):
        for j in range(z):
            abc.append(ab[i] + c[j])
    abc.sort(reverse=True)

    for i in range(k):
        print(abc[i])

=======
Suggestion 7

def main():
    x, y, z, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ab = sorted([a[i] + b[j] for i in range(x) for j in range(y)], reverse=True)[:k]
    abc = sorted([ab[i] + c[j] for i in range(k) for j in range(z)], reverse=True)[:k]
    for i in abc:
        print(i)

=======
Suggestion 8

def main():
    x, y, z, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    ab = []
    for i in range(x):
        for j in range(y):
            ab.append(a[i] + b[j])

    ab.sort(reverse=True)
    ab = ab[:k]

    abc = []
    for i in range(min(k, len(ab))):
        for j in range(z):
            abc.append(ab[i] + c[j])

    abc.sort(reverse=True)
    for i in range(k):
        print(abc[i])

=======
Suggestion 9

def main():
    #入力
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    
    #ソート
    A.sort(reverse = True)
    B.sort(reverse = True)
    C.sort(reverse = True)
    
    #計算
    AB = []
    for i in range(X):
        for j in range(Y):
            AB.append(A[i] + B[j])
    AB.sort(reverse = True)
    ABC = []
    for i in range(min(K, X * Y)):
        for j in range(Z):
            ABC.append(AB[i] + C[j])
    ABC.sort(reverse = True)
    
    #出力
    for i in range(K):
        print(ABC[i])
