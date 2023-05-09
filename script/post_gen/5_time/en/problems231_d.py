Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    A.sort()
    B.sort()

    if A[0] == 1 and B[-1] == N:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    if A[0] < B[0] and A[-1] < B[0]:
        print("Yes")
    elif A[-1] < B[-1] and A[0] < B[-1]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())

    #print(A)
    #print(B)

    A = sorted(A)
    B = sorted(B)
    #print(A)
    #print(B)

    if A[M-1] < B[0]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def solve():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    A.sort()
    B.sort()
    if A[0] == 1 and B[-1] == N:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = []
    b = []
    for i in range(m):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    a.sort()
    b.sort()
    print('Yes' if a[-1] < b[0] else 'No')

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a,b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    if A[0] == 1 and B[-1] == N:
        print("YES")
    else:
        print("NO")

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a = []
    b = []
    for i in range(m):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    a = set(a)
    b = set(b)
    if len(a & b) > 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a,b = map(int, input().split())
        A.append(a)
        B.append(b)

    #print(A)
    #print(B)

    #print("A[0] = " + str(A[0]))
    #print("B[0] = " + str(B[0]))

    #print("A[1] = " + str(A[1]))
    #print("B[1] = " + str(B[1]))

    #print("A[2] = " + str(A[2]))
    #print("B[2] = " + str(B[2]))

    #print("A[3] = " + str(A[3]))
    #print("B[3] = " + str(B[3]))

    #print("A[4] = " + str(A[4]))
    #print("B[4] = " + str(B[4]))

    #print("A[5] = " + str(A[5]))
    #print("B[5] = " + str(B[5]))

    #print("A[6] = " + str(A[6]))
    #print("B[6] = " + str(B[6]))

    #print("A[7] = " + str(A[7]))
    #print("B[7] = " + str(B[7]))

    #print("A[8] = " + str(A[8]))
    #print("B[8] = " + str(B[8]))

    #print("A[9] = " + str(A[9]))
    #print("B[9] = " + str(B[9]))

    #print("A[10] = " + str(A[10]))
    #print("B[10] = " + str(B[10]))

    #print("A[11] = " + str(A[11]))
    #print("B[11] = " + str(B[11]))

    #print("A[12] = " + str(A[12]))
    #print("B[12] = " + str(B[12]))

    #print("A[13] = " + str(A[13]))
    #print("B[13]

=======
Suggestion 9

def main():
    n,m = map(int, input().split())
    a = []
    b = []
    for i in range(m):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    a = sorted(a, reverse=True)
    b = sorted(b, reverse=True)
    if a[0] == 1 or b[0] == n:
        print("No")
    else:
        print("Yes")

=======
Suggestion 10

def main():
    n,m = map(int,input().split())
    a_b = []
    for i in range(m):
        a_b.append(list(map(int,input().split())))
    a_b.sort(key=lambda x:x[1])
    #print(a_b)
    right = a_b[0][1]
    count = 1
    for i in range(1,m):
        if right <= a_b[i][0]:
            right = a_b[i][1]
            count += 1
    if count == m:
        print('Yes')
    else:
        print('No')
