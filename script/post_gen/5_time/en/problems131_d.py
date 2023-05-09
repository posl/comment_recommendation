Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    jobs = []
    for i in range(n):
        a, b = map(int, input().split())
        jobs.append((a, b))
    jobs.sort(key=lambda x: x[1])
    time = 0
    for a, b in jobs:
        time += a
        if time > b:
            print("No")
            return
    print("Yes")

=======
Suggestion 2

def main():
    N = int(input())
    jobs = []
    for i in range(N):
        A, B = map(int, input().split())
        jobs.append((A, B))
    jobs.sort(key=lambda x: x[1])
    time = 0
    for i in range(N):
        time += jobs[i][0]
        if time > jobs[i][1]:
            print('No')
            return
    print('Yes')

=======
Suggestion 3

def main():
    N = int(input())
    jobs = []
    for i in range(N):
        A, B = map(int, input().split())
        jobs.append((A, B))
    jobs.sort(key=lambda x: x[1])
    time = 0
    for job in jobs:
        time += job[0]
        if time > job[1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 4

def main():
    n = int(input())
    job = []
    for i in range(n):
        a, b = map(int, input().split())
        job.append([a, b])
    job.sort(key=lambda x: x[1])
    time = 0
    for i in range(n):
        time += job[i][0]
        if time > job[i][1]:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 5

def main():
    n = int(input())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    c = list(zip(a, b))
    c.sort(key=lambda x: x[1])
    t = 0
    for i in range(n):
        t += c[i][0]
        if t > c[i][1]:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 6

def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x:x[1])
    t = 0
    for a, b in ab:
        t += a
        if t > b:
            print('No')
            return
    print('Yes')

=======
Suggestion 7

def main():
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    AB.sort(key=lambda x: x[1])
    time = 0
    for i in range(N):
        time += AB[i][0]
        if time > AB[i][1]:
            print("No")
            exit()
    print("Yes")

=======
Suggestion 8

def main():
    N = int(input())
    jobs = []
    for i in range(N):
        jobs.append(list(map(int, input().split())))
    jobs.sort(key=lambda x: x[1])
    time = 0
    for job in jobs:
        time += job[0]
        if time > job[1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 9

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # print(A)
    # print(B)
    C = [0] * N
    for i in range(N):
        C[i] = A[i] + B[i]
    # print(C)
    D = [0] * N
    for i in range(N):
        D[i] = C[i] - B[i]
    # print(D)
    E = [0] * N
    for i in range(N):
        E[i] = C[i] + B[i]
    # print(E)
    F = [0] * N
    for i in range(N):
        F[i] = D[i] + B[i]
    # print(F)
    G = [0] * N
    for i in range(N):
        G[i] = E[i] + B[i]
    # print(G)
    H = [0] * N
    for i in range(N):
        H[i] = F[i] + B[i]
    # print(H)
    I = [0] * N
    for i in range(N):
        I[i] = G[i] + B[i]
    # print(I)
    J = [0] * N
    for i in range(N):
        J[i] = H[i] + B[i]
    # print(J)
    K = [0] * N
    for i in range(N):
        K[i] = I[i] + B[i]
    # print(K)
    L = [0] * N
    for i in range(N):
        L[i] = J[i] + B[i]
    # print(L)
    M = [0] * N
    for i in range(N):
        M[i] = K[i] + B[i]
    # print(M)
    N = [0] * N
    for i in range(N):
        N[i] = L[i] + B[i]
    # print(N)
    O = [0] * N
    for i in range(N):
        O[i] = M[i] + B[i]
    # print(O)
    P = [0] * N
    for i in range(N):

=======
Suggestion 10

def main():
    n = int(input())
    j = [list(map(int, input().split())) for i in range(n)]
    j = sorted(j, key=lambda x: x[1])
    t = 0
    for i in range(n):
        t += j[i][0]
        if t > j[i][1]:
            print("No")
            return
    print("Yes")
