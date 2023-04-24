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
            AB.append(a+b)
    AB.sort(reverse=True)

    ABC = []
    for ab in AB[:K]:
        for c in C:
            ABC.append(ab+c)
    ABC.sort(reverse=True)

    for abc in ABC[:K]:
        print(abc)

=======
Suggestion 2

def main():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)

    ans = []
    for i in range(X):
        for j in range(Y):
            for k in range(Z):
                ans.append(A[i] + B[j] + C[k])

    ans.sort(reverse=True)

    for i in range(K):
        print(ans[i])

=======
Suggestion 3

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
    for i in range(len(ab)):
        for j in range(z):
            abc.append(ab[i] + c[j])
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

main()

=======
Suggestion 5

def main():
    x, y, z, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    a.sort(reverse=True)
    b.sort(reverse=True)
    c.sort(reverse=True)

    ans = []
    for i in range(x):
        for j in range(y):
            for k in range(z):
                ans.append(a[i] + b[j] + c[k])

    ans.sort(reverse=True)

    for i in range(k):
        print(ans[i])

=======
Suggestion 6

def main():
    x,y,z,k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    a.sort(reverse=True)
    b.sort(reverse=True)
    c.sort(reverse=True)

    ab = []
    for i in range(x):
        for j in range(y):
            ab.append(a[i]+b[j])

    ab.sort(reverse=True)

    abc = []
    for i in range(min(k, len(ab))):
        for j in range(z):
            abc.append(ab[i]+c[j])

    abc.sort(reverse=True)

    for i in range(k):
        print(abc[i])

=======
Suggestion 7

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
    for i in range(min(k,len(ab))):
        for j in range(z):
            abc.append(ab[i]+c[j])
    abc.sort(reverse=True)

    for i in range(k):
        print(abc[i])

=======
Suggestion 8

def main():
    # Get input here
    x, y, z, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    # Compute desired result here
    a.sort(reverse=True)
    b.sort(reverse=True)
    c.sort(reverse=True)

    # Print result here
    ans = []
    for i in range(x):
        for j in range(y):
            for k in range(z):
                if (i+1)*(j+1)*(k+1) <= k:
                    break
                ans.append(a[i] + b[j] + c[k])
    ans.sort(reverse=True)
    for i in range(k):
        print(ans[i])

=======
Suggestion 9

def main():
    X,Y,Z,K=map(int, input().split())
    A=list(map(int, input().split()))
    B=list(map(int, input().split()))
    C=list(map(int, input().split()))
    AB=[]
    for a in A:
        for b in B:
            AB.append(a+b)
    AB.sort()
    AB.reverse()
    ABC=[]
    for i in range(min(K,len(AB))):
        for c in C:
            ABC.append(AB[i]+c)
    ABC.sort()
    ABC.reverse()
    for i in range(K):
        print(ABC[i])
