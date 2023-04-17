Synthesizing 10/10 solutions

=======

def median(a):
    a.sort()
    if len(a) % 2 == 0:
        return (a[len(a) // 2 - 1] + a[len(a) // 2]) // 2
    else:
        return a[len(a) // 2]

n = int(input())
a = list(map(int, input().split()))
print(median(a))

=======

def main():
    N = int(input())
    A = list(map(int, input().split()))

    B = [0] * (N + 1)
    for i in range(N):
        B[i + 1] = B[i] + A[i]

    S = set(A)
    S = sorted(list(S))
    M = len(S)
    C = [0] * M
    for i in range(N):
        idx = bisect.bisect_left(S, A[i])
        C[idx] += 1

    D = [0] * (M + 1)
    for i in range(M):
        D[i + 1] = D[i] + C[i]

    ans = 0
    for i in range(N):
        idx = bisect.bisect_left(S, A[i])
        ans += (B[N] - B[i + 1]) - (S[idx] * (D[M] - D[idx]))
        ans -= ((S[idx] * D[idx]) - (B[i + 1] - B[0]))
    print(ans // N)

=======

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(n):
        b.append((a[i], i))
    b.sort()
    c = [0] * n
    for i in range(n):
        c[b[i][1]] = i
    ans = 0
    for i in range(n):
        ans += (n - i - 1) * c[i] - i * c[i]
    print(ans)

=======

def median(a):
    a.sort()
    return a[len(a)//2]

N = int(input())
A = list(map(int, input().split()))

B = []
for i in range(N):
    for j in range(i, N):
        B.append(median(A[i:j+1]))

print(median(B))

I tried to solve this problem, but I got WA. I think that my code is correct, but I don't know why I got WA. Could you please tell me why I got WA?

I got AC with this code.

=======

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = sorted(A)
    C = [0] * N
    for i in range(N):
        C[i] = B.index(A[i])
    D = [0] * N
    for i in range(N):
        D[C[i]] = i
    E = [0] * N
    for i in range(N):
        E[i] = D[i] - C[i]
    F = [0] * N
    for i in range(N):
        F[i] = E[i] + i
    print(B[N//2])

main()

=======

def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    B = sorted(A)
    C = [0] * N
    for i in range(N):
        C[i] = B.index(A[i])
    print(C)

=======

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    l = a[n//2-1]
    r = a[n//2]
    for i in range(n):
        if a[i] > l:
            print(l)
        else:
            print(r)

=======

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = sorted(A)
    C = [0] * N
    for i in range(N):
        C[i] = (B[N // 2 - 1] + B[N // 2]) // 2
    D = [0] * N
    for i in range(N):
        D[i] = B[i] - C[i]
    E = [0] * N
    for i in range(N):
        E[i] = D[i] + E[i - 1]
    F = [0] * N
    for i in range(N):
        F[i] = E[i] - (i + 1) * D[i]
    G = sorted(F)
    print(G[N // 2] + C[0])

=======

def median(b):
    b.sort()
    return b[len(b) // 2]

=======

def median(lst):
    lst = sorted(lst)
    return lst[len(lst)//2]
