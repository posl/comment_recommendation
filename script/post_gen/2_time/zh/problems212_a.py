Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())

    print(N, M, A, B)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])
    now = 0
    ans = 1
    for a, b in AB:
        if a > now:
            now = b - 1
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    print(A)
    print(B)
    print(N)
    print(M)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])
    # print(AB)
    ans = 0
    end = 0
    for a, b in AB:
        if a > end:
            ans += 1
            end = b - 1
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])
    ans = 0
    now = 0
    for a, b in AB:
        if a > now:
            now = b - 1
            ans += 1
    print(ans)

=======
Suggestion 6

def search(x):
    if x == 1:
        return 1
    elif x == 2:
        return 0
    else:
        if x in dict:
            return dict[x]
        else:
            dict[x] = search(x-1) + search(x-2)
            return dict[x]

N,M = map(int,input().split())
dict = {}
for i in range(M):
    A,B = map(int,input().split())
    if A in dict:
        dict[A] += 1
    else:
        dict[A] = 1
    if B in dict:
        dict[B] += 1
    else:
        dict[B] = 1
print(dict)
print(search(N))

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a = []
    b = []
    for i in range(m):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    print(a)
    print(b)
    ans = 0
    for i in range(m):
        if a[i] == 1 or b[i] == n:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # print(A)
    # print(B)
    # print(N)
    # print(M)
    # print(len(A))
    # print(len(B))
    # print(A[0])
    # print(B[0])
    # print(A[1])
    # print(B[1])
    # print(A[2])
    # print(B[2])
    # print(A[3])
    # print(B[3])
    # print(A[4])
    # print(B[4])
    # print(A[5])
    # print(B[5])
    # print(A[6])
    # print(B[6])
    # print(A[7])
    # print(B[7])
    # print(A[8])
    # print(B[8])
    # print(A[9])
    # print(B[9])
    # print(A[10])
    # print(B[10])
    # print(A[11])
    # print(B[11])
    # print(A[12])
    # print(B[12])
    # print(A[13])
    # print(B[13])
    # print(A[14])
    # print(B[14])
    # print(A[15])
    # print(B[15])
    # print(A[16])
    # print(B[16])
    # print(A[17])
    # print(B[17])
    # print(A[18])
    # print(B[18])
    # print(A[19])
    # print(B[19])
    # print(A[20])
    # print(B[20])
    # print(A[21])
    # print(B[21])
    # print(A[22])
    # print(B[22])
    # print(A[23])
    # print(B[23])
    # print(A[24])
    # print(B[24])
    # print(A[25])
    # print(B[25])
    # print(A[26])
    # print(B[26])
    # print(A[27])
    # print(B[27])
    # print(A[28])
    # print(B[28])
    # print(A[29])
    # print(B

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB = sorted(AB, key=lambda x:x[1])
    ans = 0
    pre = 0
    for ab in AB:
        if ab[0] > pre:
            ans += 1
            pre = ab[1] - 1
    print(ans)

=======
Suggestion 10

def main():
    N,M = map(int,input().split())
    AB = [list(map(int,input().split())) for i in range(M)]
    AB.sort(key=lambda x:x[0])
    #print(AB)
    #print(N,M)
    #print(AB)
    #print(AB[0][1])

    #print(AB[0][0])
    #print(AB[0][1])

    #print(AB[1][0])
    #print(AB[1][1])

    #print(AB[2][0])
    #print(AB[2][1])

    #print(AB[3][0])
    #print(AB[3][1])

    #print(AB[4][0])
    #print(AB[4][1])

    #print(AB[5][0])
    #print(AB[5][1])

    #print(AB[6][0])
    #print(AB[6][1])

    #print(AB[7][0])
    #print(AB[7][1])

    #print(AB[8][0])
    #print(AB[8][1])

    #print(AB[9][0])
    #print(AB[9][1])

    #print(AB[10][0])
    #print(AB[10][1])

    #print(AB[11][0])
    #print(AB[11][1])

    #print(AB[12][0])
    #print(AB[12][1])

    #print(AB[13][0])
    #print(AB[13][1])

    #print(AB[14][0])
    #print(AB[14][1])

    #print(AB[15][0])
    #print(AB[15][1])

    #print(AB[16][0])
    #print(AB[16][1])

    #print(AB[17][0])
    #print(AB[17][1])

    #print(AB[18][0])
    #print(AB[18][1])

    #print(AB[19][0])
    #print(AB[19][1])

    #print(AB[20][0])
    #print(AB[20][1])

    #print(AB[21][0])
    #print
