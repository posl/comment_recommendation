Synthesizing 10/10 solutions

=======
Suggestion 1

def readinput():
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))
    return n,a,b,c

=======
Suggestion 2

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    C = [int(x) for x in input().split()]

    #print(N)
    #print(A)
    #print(B)
    #print(C)

    cnt = 0
    for i in range(1, N+1):
        cnt += B[C[i-1]-1] == A[i-1]

    print(cnt)

=======
Suggestion 3

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    count = 0
    d = [0] * (n + 1)
    for i in range(n):
        d[b[c[i] - 1]] += 1
    for i in range(n):
        count += d[a[i]]
    print(count)

=======
Suggestion 4

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    C = [int(i) for i in input().split()]

    D = [0] * N

    for i in range(N):
        D[B[C[i]-1]-1] += 1

    count = 0
    for i in range(N):
        count += D[A[i]-1]

    print(count)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(lambda x: int(x) - 1, input().split()))
    d = [0] * n
    for i in range(n):
        d[b[c[i]]] += 1
    ans = 0
    for i in range(n):
        ans += d[a[i]]
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    A.sort()
    B.sort()
    C.sort()

    count = 0

    for i in range(N):
        count += len([j for j in range(N) if A[i] == B[C[j] - 1]])

    print(count)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    count = 0
    for i in range(N):
        count += B[C[i]-1] == A[i]

    print(count)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))

    a.sort()
    b.sort()
    c.sort()

    ans = 0

    for i in range(n):
        ans += (bisect.bisect_left(a,b[i])) * (n - bisect.bisect_right(c,b[i]))

    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    B_C = [0] * (N + 1)
    for j in range(N):
        B_C[C[j]] += 1

    A_B_C = [0] * (N + 1)
    for i in range(N):
        A_B_C[A[i]] += B_C[i + 1]

    print(sum(A_B_C))

=======
Suggestion 10

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    B_dict = {}
    for i in range(N):
        b = B[i]
        if b in B_dict:
            B_dict[b].append(i)
        else:
            B_dict[b] = [i]

    C_dict = {}
    for i in range(N):
        c = C[i]
        if c in C_dict:
            C_dict[c].append(i)
        else:
            C_dict[c] = [i]

    count = 0
    for a in A:
        if a in B_dict:
            for b_i in B_dict[a]:
                if C[b_i] in C_dict:
                    count += len(C_dict[C[b_i]])

    return count

print(solve())
