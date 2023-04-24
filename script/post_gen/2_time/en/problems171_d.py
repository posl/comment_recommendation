Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = []
    C = []
    for i in range(Q):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)
    S = sum(A)
    for i in range(Q):
        b = B[i]
        c = C[i]
        count = A.count(b)
        S += count * (c - b)
        print(S)

main()

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = []
    C = []
    for i in range(Q):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)

    sum = 0
    for a in A:
        sum += a
    #print(sum)
    for i in range(Q):
        count = 0
        for a in A:
            if a == B[i]:
                count += 1
        sum += (C[i] - B[i]) * count
        print(sum)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = []
    C = []
    for i in range(Q):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)
    for i in range(Q):
        A = [c if a == b else a for a, b, c in zip(A, [B[i]] * N, [C[i]] * N)]
        print(sum(A))

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    b = [0]*q
    c = [0]*q
    for i in range(q):
        b[i], c[i] = map(int, input().split())
    count = [0]*10**5
    for i in range(n):
        count[a[i]-1] += 1
    sum = 0
    for i in range(n):
        sum += a[i]
    for i in range(q):
        sum += (c[i]-b[i])*count[b[i]-1]
        count[c[i]-1] += count[b[i]-1]
        count[b[i]-1] = 0
        print(sum)

=======
Suggestion 5

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    Q = int(input())
    B = [0] * Q
    C = [0] * Q
    for i in range(Q):
        B[i], C[i] = [int(x) for x in input().split()]
    S = sum(A)
    for i in range(Q):
        S += (C[i] - B[i]) * A.count(B[i])
        print(S)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = []
    C = []
    for _ in range(Q):
        b, c = list(map(int, input().split()))
        B.append(b)
        C.append(c)
    sum_A = sum(A)
    count_B = [0] * (10**5 + 1)
    for a in A:
        count_B[a] += 1
    for i in range(Q):
        sum_A += (C[i] - B[i]) * count_B[B[i]]
        count_B[C[i]] += count_B[B[i]]
        count_B[B[i]] = 0
        print(sum_A)

=======
Suggestion 7

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    Q = int(input())
    B = [0]*Q
    C = [0]*Q
    for i in range(Q):
        B[i], C[i] = [int(x) for x in input().split()]
    #print(N,A,Q,B,C)
    sumA = sum(A)
    #print(sumA)
    for i in range(Q):
        count = A.count(B[i])
        sumA = sumA + count*(C[i]-B[i])
        print(sumA)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    #print(N, A, Q, BC)

    B = [0] * (10**5+1)
    for a in A:
        B[a] += 1

    S = sum(A)
    for b, c in BC:
        S += (c-b) * B[b]
        B[c] += B[b]
        B[b] = 0
        print(S)

=======
Suggestion 9

def main():
    #input
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    #solve
    ans = [0] * Q
    B = [0] * (10**5+1)
    for a in A:
        B[a] += 1
    S = sum(A)
    for i in range(Q):
        b, c = BC[i]
        S -= B[b] * b
        S += B[b] * c
        B[c] += B[b]
        B[b] = 0
        ans[i] = S
    #output
    for a in ans:
        print(a)
