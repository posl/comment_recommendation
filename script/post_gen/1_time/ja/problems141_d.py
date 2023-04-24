Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    for i in range(M):
        A[i] = A[i] // 2
    print(sum(A))

=======
Suggestion 2

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    for i in range(M):
        A[0] = A[0]//2
        A.sort(reverse=True)
    print(sum(A))

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(M):
        A[N-1] = A[N-1] // 2
        A.sort()
    print(sum(A))

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    for i in range(n):
        a[i] = a[i] * 2
    for i in range(m):
        a[0] = a[0] // 2
        a.sort(reverse=True)
    print(sum(a))

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)

    for i in range(n):
        a[i] = a[i] / 2

    for i in range(m):
        a.append(a.pop() / 2)

    print(int(sum(a)))

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    #print(a)
    for i in range(m):
        a[0] = a[0]//2
        a.sort(reverse=True)
        #print(a)
    print(sum(a))

main()

=======
Suggestion 7

def calc(n, m, a):
    a.sort(reverse=True)
    for i in range(m):
        a[0] = a[0] // 2
        a.sort(reverse=True)
    return sum(a)

n, m = map(int, input().split())
a = list(map(int, input().split()))
print(calc(n, m, a))

=======
Suggestion 8

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    B = []
    for i in range(N):
        if A[i] == 0:
            continue
        else:
            B.append(A[i])
    B.sort()
    for i in range(M):
        if len(B) == 0:
            break
        else:
            B[0] = B[0] // 2
            if B[0] == 0:
                del B[0]
            else:
                B.sort()
    print(sum(B))

=======
Suggestion 9

def get_ints(): return map(int, input().split())

=======
Suggestion 10

def f(x, a, m):
    for i in range(m):
        x = x // 2
    return x
