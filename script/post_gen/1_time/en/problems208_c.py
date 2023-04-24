Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    x = k // n
    y = k % n
    for i in range(n):
        if i < y:
            print(x + 1)
        else:
            print(x)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = []
    for i in range(n):
        b.append((i, a[i]))
    b.sort(key=lambda x: x[1])
    c = [k // n] * n
    k %= n
    for i in range(k):
        c[b[i][0]] += 1
    for i in range(n):
        print(c[i])

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N):
        if i < K % N:
            print(K // N + 1)
        else:
            print(K // N)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = [0] * n
    for i in range(n):
        b[i] = k // n
    for i in range(k % n):
        b[i] += 1
    for i in range(n):
        print(b[a.index(a[i])])

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = k // n
    mod = k % n
    for i in range(n):
        if i < mod:
            print(ans + 1)
        else:
            print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = [K // N] * N
    K %= N
    for i in range(K):
        B[A[i]-1] += 1
    for i in range(N):
        print(B[i])

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N):
        if K > N:
            print(1)
        else:
            if i < K:
                print(1)
            else:
                print(0)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    k = k % n
    for i in range(n):
        if i < k:
            print(n)
        else:
            print(n-1)

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * n
    c = k // n
    k %= n
    for i in range(n):
        b[i] = c
    d = sorted(a)
    for i in range(k):
        b[a.index(d[i])] += 1
    for i in range(n):
        print(b[i])

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    As = list(map(int, input().split()))
    sorted_As = sorted(As)
    #print(sorted_As)
    Ks = [K//N]*N
    #print(Ks)
    K = K%N
    #print(K)
    for i in range(0, K):
        Ks[As.index(sorted_As[i])] += 1
    #print(Ks)
    for i in range(0, N):
        print(Ks[i])
