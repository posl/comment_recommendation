Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort(reverse=True)

    for i in range(K):
        A[B[i]-1] = 0

    if max(A) == 0:
        print("No")
    else:
        print("Yes")

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort(reverse=True)

    for i in range(K):
        A[B[i]-1] = 0

    print(sum(A))

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for i in range(k):
        a[b[i]-1] = 0

    if max(a) > 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    maxA = max(A)
    maxB = max(B)

    if maxA > maxB:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    #n, k = map(int, input().split())
    #a = list(map(int, input().split()))
    #b = list(map(int, input().split()))
    n, k = 5, 3
    a = [6, 8, 10, 7, 10]
    b = [2, 3, 4]
    #n, k = 5, 2
    #a = [100, 100, 100, 1, 1]
    #b = [5, 4]
    #n, k = 2, 1
    #a = [100, 1]
    #b = [2]
    #n, k = 5, 3
    #a = [6, 8, 10, 7, 10]
    #b = [2, 3, 4]
    #n, k = 5, 2
    #a = [100, 100, 100, 1, 1]
    #b = [5, 4]
    #n, k = 2, 1
    #a = [100, 1]
    #b = [2]
    #n, k = 5, 3
    #a = [6, 8, 10, 7, 10]
    #b = [2, 3, 4]
    #n, k = 5, 2
    #a = [100, 100, 100, 1, 1]
    #b = [5, 4]
    #n, k = 2, 1
    #a = [100, 1]
    #b = [2]
    #n, k = 5, 3
    #a = [6, 8, 10, 7, 10]
    #b = [2, 3, 4]
    #n, k = 5, 2
    #a = [100, 100, 100, 1, 1]
    #b = [5, 4]
    #n, k = 2, 1
    #a = [100, 1]
    #b = [2]
    #n, k = 5

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    c = [0] * n
    for i in range(k):
        c[b[i]-1] = 1
    d = []
    for i in range(n):
        if c[i] == 0:
            d.append(a[i])
    d.sort(reverse=True)
    for i in range(k):
        d.pop()
    if len(d) == 0:
        print('No')
    else:
        if max(d) > max(a):
            print('Yes')
        else:
            print('No')

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort(reverse=True)
    b.sort(reverse=True)

    for i in range(k):
        if a[i] > b[i]:
            print("Yes")
            return
    print("No")

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    max_a = max(A)
    max_b = max(B)

    if max_a > max_b:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print("Yes" if len(set(b) & set(sorted(a, reverse=True)[:k])) > 0 else "No")

=======
Suggestion 10

def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    a = sorted(a,reverse=True)
    b = sorted(b)

    for i in range(k):
        if a[i] < b[i]:
            print("Yes")
            exit()

    print("No")
main()
