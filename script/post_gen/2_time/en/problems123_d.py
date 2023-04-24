Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ABC = []
    for a in A:
        for b in B:
            ABC.append(a+b)
    ABC.sort(reverse=True)
    ABC = ABC[:K]
    ABC2 = []
    for abc in ABC:
        for c in C:
            ABC2.append(abc+c)
    ABC2.sort(reverse=True)
    ABC2 = ABC2[:K]
    for abc2 in ABC2:
        print(abc2)

main()

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
    for i in range(K):
        print(ABC[i])

main()

I got AC. I think this solution is not so efficient because I used 3 nested loops. But I couldn’t find any other way to solve this problem. If you have any idea, please let me know.

Thank you for reading my blog.

=======
Suggestion 3

def main():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    AB = sorted([a + b for a in A for b in B], reverse = True)[:K]
    ABC = sorted([a + b for a in AB for b in C], reverse = True)[:K]
    print('\n'.join(map(str, ABC)))

=======
Suggestion 4

def main():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    AB = sorted([a + b for a in A for b in B], reverse=True)
    ABC = sorted([ab + c for ab in AB[:K] for c in C], reverse=True)

    for i in range(K):
        print(ABC[i])

=======
Suggestion 5

def main():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)

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
Suggestion 6

def solve():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    AB = []
    for a in A:
        for b in B:
            AB.append(a + b)
    AB.sort(reverse=True)
    AB = AB[:K]
    ABC = []
    for ab in AB:
        for c in C:
            ABC.append(ab + c)
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
  A.sort(reverse=True)
  B.sort(reverse=True)
  C.sort(reverse=True)
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
  for i in range(K):
    print(ABC[i])

main()

=======
Suggestion 8

def main():
    x, y, z, k = map(int, input().split())
    a = sorted(list(map(int, input().split())), reverse=True)
    b = sorted(list(map(int, input().split())), reverse=True)
    c = sorted(list(map(int, input().split())), reverse=True)
    ab = sorted([a[i] + b[j] for i in range(x) for j in range(y)], reverse=True)
    abc = sorted([ab[i] + c[j] for i in range(min(x * y, k)) for j in range(z)], reverse=True)
    for i in range(k):
        print(abc[i])

=======
Suggestion 9

def main():
    import heapq
    x, y, z, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ab = []
    for i in a:
        for j in b:
            ab.append(i + j)
    ab.sort(reverse=True)
    ab = ab[:k]
    abc = []
    for i in ab:
        for j in c:
            abc.append(i + j)
    abc.sort(reverse=True)
    for i in abc[:k]:
        print(i)

=======
Suggestion 10

def solve(X, Y, Z, K, A, B, C):
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
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
