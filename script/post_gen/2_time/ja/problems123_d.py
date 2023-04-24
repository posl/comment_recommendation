Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    AB = [a + b for a in A for b in B]
    AB.sort(reverse=True)
    ABC = [ab + c for ab in AB[:K] for c in C]
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
    AB = [a+b for a in A for b in B]
    AB.sort(reverse=True)
    AB = AB[:K]
    ABC = [ab+c for ab in AB for c in C]
    ABC.sort(reverse=True)
    ABC = ABC[:K]
    for abc in ABC:
        print(abc)

=======
Suggestion 3

def main():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    AB = sorted([a + b for a in A for b in B], reverse=True)[:K]
    ABC = sorted([ab + c for ab in AB for c in C], reverse=True)[:K]
    for abc in ABC:
        print(abc)

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
    S = []
    for i in range(X):
        for j in range(Y):
            S.append(A[i] + B[j])
    S.sort(reverse=True)
    T = []
    for i in range(min(K, X * Y)):
        for j in range(Z):
            T.append(S[i] + C[j])
    T.sort(reverse=True)
    for i in range(K):
        print(T[i])

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
    AB.sort(reverse=True)
    ABC = []
    for ab in AB[:K]:
        for c in C:
            ABC.append(ab + c)
    ABC.sort(reverse=True)
    for abc in ABC[:K]:
        print(abc)

=======
Suggestion 6

def main():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    AB = [a + b for a in A for b in B]
    AB.sort(reverse=True)
    ABC = [ab + c for ab in AB[:K] for c in C[:K]]
    ABC.sort(reverse=True)
    for i in range(K):
        print(ABC[i])

=======
Suggestion 7

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
Suggestion 8

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

    for ans in ABC[:K]:
        print(ans)

=======
Suggestion 9

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
    for i in range(min(k, x * y)):
        for j in range(z):
            abc.append(ab[i] + c[j])
    abc.sort(reverse=True)
    for i in range(k):
        print(abc[i])
