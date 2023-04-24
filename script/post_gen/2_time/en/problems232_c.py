Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(M)]
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(N):
                for l in range(k + 1, N):
                    if AB.count([i + 1, j + 1]) == AB.count([k + 1, l + 1]) and CD.count([i + 1, j + 1]) == CD.count([k + 1, l + 1]):
                        continue
                    else:
                        print("No")
                        return
    print("Yes")
    return

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    C = [0] * M
    D = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    for i in range(M):
        C[i], D[i] = map(int, input().split())
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(M):
                if A[k] == i + 1 and B[k] == j + 1:
                    a = k
                if A[k] == j + 1 and B[k] == i + 1:
                    b = k
            for k in range(M):
                if C[k] == i + 1 and D[k] == j + 1:
                    c = k
                if C[k] == j + 1 and D[k] == i + 1:
                    d = k
            if (a == c and b == d) or (a == d and b == c):
                continue
            else:
                print("No")
                return
    print("Yes")
    return

main()

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(M)]
    CD = [list(map(int, input().split())) for i in range(M)]

    for i in range(M):
        AB[i][0] -= 1
        AB[i][1] -= 1
        CD[i][0] -= 1
        CD[i][1] -= 1

    for i in range(N):
        for j in range(N):
            for k in range(N):
                for l in range(N):
                    if i == j or i == k or i == l or j == k or j == l or k == l:
                        continue
                    if AB[0][0] == i and AB[0][1] == j and CD[0][0] == k and CD[0][1] == l:
                        P = [i, j, k, l]
                        flag = 1
                        for m in range(M):
                            if AB[m][0] == P[AB[m][1]]:
                                if CD[m][0] == P[CD[m][1]]:
                                    continue
                                else:
                                    flag = 0
                                    break
                            else:
                                if CD[m][0] == P[CD[m][1]]:
                                    flag = 0
                                    break
                                else:
                                    continue
                        if flag == 1:
                            print("Yes")
                            exit()
    print("No")

=======
Suggestion 4

def solve():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(M)]
    B = [list(map(int, input().split())) for _ in range(M)]
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(M):
                if (A[k][0] == i + 1 and A[k][1] == j + 1) or (A[k][0] == j + 1 and A[k][1] == i + 1):
                    if (B[k][0] == i + 1 and B[k][1] == j + 1) or (B[k][0] == j + 1 and B[k][1] == i + 1):
                        continue
                    else:
                        print("No")
                        return
                elif (B[k][0] == i + 1 and B[k][1] == j + 1) or (B[k][0] == j + 1 and B[k][1] == i + 1):
                    if (A[k][0] == i + 1 and A[k][1] == j + 1) or (A[k][0] == j + 1 and A[k][1] == i + 1):
                        continue
                    else:
                        print("No")
                        return
    print("Yes")
    return

=======
Suggestion 5

def permute(a, l, r):
    if l == r:
        print(a)
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    if M == 0:
        print("Yes")
        return
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    CD = [tuple(map(int, input().split())) for _ in range(M)]
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(M):
                if AB[k][0] == i + 1 and AB[k][1] == j + 1:
                    AB[k] = (i, j)
                elif AB[k][0] == j + 1 and AB[k][1] == i + 1:
                    AB[k] = (j, i)
                if CD[k][0] == i + 1 and CD[k][1] == j + 1:
                    CD[k] = (i, j)
                elif CD[k][0] == j + 1 and CD[k][1] == i + 1:
                    CD[k] = (j, i)
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(N):
                for l in range(k + 1, N):
                    for m in range(M):
                        if AB[m][0] == i and AB[m][1] == j and CD[m][0] == k and CD[m][1] == l:
                            break
                    else:
                        print("No")
                        return
    print("Yes")
    return

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    #print(N, M)
    AB = []
    CD = []
    for i in range(M):
        AB.append(list(map(int, input().split())))
    for i in range(M):
        CD.append(list(map(int, input().split())))
    #print(AB)
    #print(CD)

    #Takahashi's toy is illustrated on the left in the figure below, and Aoki's is illustrated on the right.
    #The following figure shows that the two toys have the same shape. The condition in the statement is satisfied when P = (3, 2, 1, 4), for example.
    #The two toys do not have the same shape.
    #The two toys do not have the same shape.
    #print(P)
    #print(AB)
    #print(CD)
    #print(P[AB[i][0]-1], P[AB[i][1]-1])
    #print(P[CD[i][0]-1], P[CD[i][1]-1])
    #print(P[AB[i][0]-1], P[AB[i][1]-1])
    #print(P[CD[i][0]-1], P[CD[i][1]-1])
    #print(P[AB[i][0]-1], P[AB[i][1]-1])
    #print(P[CD[i][0]-1], P[CD[i][1]-1])
    #print(P[AB[i][0]-1], P[AB[i][1]-1])
    #print(P[CD[i][0]-1], P[CD[i][1]-1])
    #print(P[AB[i][0]-1], P[AB[i][1]-1])
    #print(P[CD[i][0]-1], P[CD[i][1]-1])
    #print(P[AB[i][0]-1], P[AB[i][1]-1])
    #print(P[CD[i][0]-1], P[CD[i][1]-1])
    #print(P[AB[i][0]-1], P[AB[i][1]-1])
    #print(P[CD[i][0]-1], P[CD[i][1]-1])
    #print(P[AB[i][0]-1], P[AB[i][1]-1])

=======
Suggestion 8

def check(a,b,c,d):
    for i in range(len(a)):
        if a[i] == c[i]:
            continue
        else:
            return False
    for i in range(len(b)):
        if b[i] == d[i]:
            continue
        else:
            return False
    return True

=======
Suggestion 9

def isSameShape(N,M,A,B,C,D):
    for i in range(N):
        for j in range(i+1,N):
            if (A[i] in C[j] and A[j] in C[i]) or (A[i] in D[j] and A[j] in D[i]):
                continue
            else:
                return False
    return True

=======
Suggestion 10

def find_permutation(n,m,a,b,c,d):
    if m==0:
        return True
    for i in range(n):
        for j in range(n):
            if i!=j:
                if (a[i][j] and not c[i][j]) or (not a[i][j] and c[i][j]):
                    return False
    return True
