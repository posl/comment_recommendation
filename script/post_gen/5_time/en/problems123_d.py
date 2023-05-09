Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

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
    for c in C:
        for ab in AB[:K]:
            ABC.append(ab+c)
    ABC.sort(reverse=True)
    for abc in ABC[:K]:
        print(abc)

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
Suggestion 4

def main():
    x, y, z, k = map(int, input().split())
    a = sorted(list(map(int, input().split())), reverse=True)
    b = sorted(list(map(int, input().split())), reverse=True)
    c = sorted(list(map(int, input().split())), reverse=True)
    ans = []
    for i in range(x):
        for j in range(y):
            for l in range(z):
                ans.append(a[i] + b[j] + c[l])
    ans.sort(reverse=True)
    for i in range(k):
        print(ans[i])

=======
Suggestion 5

def main():
    X, Y, Z, K = map(int, input().split())
    A = sorted(list(map(int, input().split())), reverse=True)
    B = sorted(list(map(int, input().split())), reverse=True)
    C = sorted(list(map(int, input().split())), reverse=True)
    ans = []
    for i in range(X):
        for j in range(Y):
            for k in range(Z):
                if (i+1)*(j+1)*(k+1) <= K:
                    ans.append(A[i]+B[j]+C[k])
                else:
                    break
    ans.sort(reverse=True)
    for i in range(K):
        print(ans[i])

=======
Suggestion 6

def main():
    X, Y, Z, K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    AB = [a+b for a in A for b in B]
    AB.sort(reverse=True)
    ABC = [ab+c for ab in AB[:K] for c in C]
    ABC.sort(reverse=True)
    for i in range(K):
        print(ABC[i])

=======
Suggestion 7

def main():
    # Get input
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    # Sort in descending order
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)

    # Calculate the sum of the deliciousness of the cakes
    # for the first, second, ..., K-th ways
    ans = []
    for i in range(X):
        for j in range(Y):
            for k in range(Z):
                ans.append(A[i] + B[j] + C[k])

    # Sort in descending order
    ans.sort(reverse=True)

    # Output
    for i in range(K):
        print(ans[i])

=======
Suggestion 8

def main():
    # Get input here
    X, Y, Z, K = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    C = [int(x) for x in input().split()]

    # Compute result here
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)

    ans = []
    for i in range(X):
        for j in range(Y):
            for k in range(Z):
                if (i+1)*(j+1)*(k+1) <= K:
                    ans.append(A[i]+B[j]+C[k])
                else:
                    break
    ans.sort(reverse=True)
    for i in range(K):
        print(ans[i])

=======
Suggestion 9

def solve():
    pass
