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

    for abc in ABC[:K]:
        print(abc)

=======
Suggestion 2

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

    for i in range(k):
        print(abc[i])

main()

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

    abc = []
    for i in range(min(k, x*y)):
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
    for i in range(min(x*y, k)):
        for j in range(z):
            abc.append(ab[i] + c[j])

    abc.sort(reverse=True)

    for i in range(k):
        print(abc[i])

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
                if (i+1)*(j+1)*(k+1) <= k:
                    ans.append(a[i]+b[j]+c[k])
                else:
                    break
    ans.sort(reverse=True)
    for i in range(k):
        print(ans[i])

=======
Suggestion 6

def main():
    # input
    X, Y, Z, K = map(int, input().split())
    As = list(map(int, input().split()))
    Bs = list(map(int, input().split()))
    Cs = list(map(int, input().split()))

    # compute

    # output
    print('Yes' if As[0] < Bs[0] < Cs[0] else 'No')

=======
Suggestion 7

def main():
    x,y,z,k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    abc = []
    for i in range(x):
        for j in range(y):
            abc.append(a[i]+b[j])
    abc.sort(reverse=True)
    abc = abc[:k]

    abcc = []
    for i in range(len(abc)):
        for j in range(z):
            abcc.append(abc[i] + c[j])
    abcc.sort(reverse=True)
    abcc = abcc[:k]

    for i in range(k):
        print(abcc[i])
