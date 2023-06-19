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

    A = sorted(A)
    B = sorted(B)

    if A[0] <= B[-1]:
        print(0)
    else:
        print(N - 1)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])
    ans = 0
    for i in range(M):
        if AB[i][0] == 1:
            ans += 1
        if AB[i][1] == N:
            break
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(M)]
    AB.sort(key=lambda x: x[1])
    # print(AB)
    count = 0
    for i in range(M):
        if AB[i][0] == 1:
            count += 1
        else:
            break
    # print(count)
    if count == 0:
        print(0)
        exit()
    else:
        count += 1
    end = AB[count - 1][1]
    # print(end)
    for i in range(count, M):
        if AB[i][0] <= end:
            continue
        else:
            count += 1
            end = AB[i][1]
    print(count)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])

    ans = 0
    now = 0
    for a, b in AB:
        if a > now:
            now = b-1
            ans += 1
    print(ans)

=======
Suggestion 5

def solve(n,m,ab):
    #n,m = map(int,input().split())
    #ab = [list(map(int,input().split())) for i in range(m)]
    #print(n,m,ab)
    ab.sort(key=lambda x:x[1])
    #print(ab)
    #print(ab[0][1])
    #print(ab[1][1])
    #print(ab[2][1])
    #print(ab[3][1])
    #print(ab[4][1])
    #print(ab[5][1])
    #print(ab[6][1])
    #print(ab[7][1])
    ans = 0
    if ab[0][0] == 1:
        ans += 1
    for i in range(1,m):
        if ab[i][0] >= ab[i-1][1]:
            ans += 1
    return ans

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    #print(N, M)
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        #print(a, b)
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #print(A[1])
    #print(B[1])
    #print(A[1] == 1)
    #print(B[1] == N)
    #print(A[1] == 1 and B[1] == N)
    #print(A[1] == 1 or B[1] == N)
    #print(A[1] == 1 or B[1] == N or A[1] == 1 and B[1] == N)
    #print(A[1] == 1 or B[1] == N or A[1] == 1 and B[1] == N or A[2] == 1 or B[2] == N or A[2] == 1 and B[2] == N)
    #print(A[1] == 1 or B[1] == N or A[1] == 1 and B[1] == N or A[2] == 1 or B[2] == N or A[2] == 1 and B[2] == N or A[3] == 1 or B[3] == N or A[3] == 1 and B[3] == N)
    #print(A[1] == 1 or B[1] == N or A[1] == 1 and B[1] == N or A[2] == 1 or B[2] == N or A[2] == 1 and B[2] == N or A[3] == 1 or B[3] == N or A[3] == 1 and B[3] == N or A[4] == 1 or B[4] == N or A[4] == 1 and B[4] == N)
    #print(A[1] == 1 or B[1] == N or A[1] == 1 and B[1] == N or A[2] == 1 or B

=======
Suggestion 7

def main():
    N,M = map(int,input().split())
    A = []
    B = []
    for i in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    print(A)
    print(B)
    print(N)
    print(M)
    return

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]

    AB.sort(key=lambda x: x[1])
    AB.sort(key=lambda x: x[0])

    #print(AB)

    count = 0
    now = 0
    for i in range(M):
        if AB[i][0] > now:
            count += 1
            now = AB[i][1]
        elif AB[i][1] < now:
            now = AB[i][1]

    print(count)

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    a = [0] * n
    b = [0] * n
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    a.sort()
    b.sort()
    ans = 0
    for i in range(m):
        if a[i] != a[i-1]:
            ans += 1
        if b[i] != b[i-1]:
            ans += 1
    print(ans)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort(key=lambda x: x[1])
    #print(AB)
    ans = 0
    tmp = 0
    for i in range(M):
        if AB[i][0] == 1:
            tmp += 1
            if AB[i][1] == N:
                ans += 1
        else:
            if tmp > 0:
                ans += 1
            break
    print(ans)
