Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0] + x[1], reverse=True)
    A, B = 0, 0
    for i in range(N):
        if i % 2 == 0:
            A += AB[i][0]
        else:
            B += AB[i][1]
    print(A - B)

=======
Suggestion 2

def main():
    n = int(input())
    a, b = [], []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    ans = 0
    for i in range(n):
        ans += min(a[i], b[i])
    print(ans)
    return

=======
Suggestion 3

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

    votes = 0
    for i in range(N):
        votes += A[i]

    # print(votes)

    votes = 0
    for i in range(N):
        votes += A[i]

    # print(votes)

    votes = 0
    for i in range(N):
        votes += A[i]

    # print(votes)

    votes = 0
    for i in range(N):
        votes += A[i]

    # print(votes)

=======
Suggestion 4

def main():
    n = int(input())
    a_b = []
    for i in range(n):
        a_b.append(list(map(int,input().split())))
    a_b.sort(key=lambda x:x[0]+x[1],reverse=True)
    a = 0
    b = 0
    for i in range(n):
        a += a_b[i][0]
    for i in range(n):
        b += a_b[i][1]
        a -= a_b[i][0]
        if a < b:
            print(i+1)
            return
    print(n)

=======
Suggestion 5

def main():
    n=int(input())
    a=[]
    b=[]
    for i in range(n):
        line=input()
        a.append(int(line.split()[0]))
        b.append(int(line.split()[1]))
    #print(a)
    #print(b)
    count=0
    for i in range(n):
        if a[i]>b[i]:
            count+=1
    print(count)

=======
Suggestion 6

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a1, b1 = map(int, input().split())
        a.append(a1)
        b.append(b1)
    a.sort()
    b.sort()
    if n % 2 == 1:
        mid = n // 2
        print(b[mid] - a[mid] + 1)
    else:
        mid = n // 2
        print(b[mid] + b[mid - 1] - a[mid] - a[mid - 1] + 1)

=======
Suggestion 7

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    if N % 2 == 0:
        a = A[N//2-1] + A[N//2]
        b = B[N//2-1] + B[N//2]
        print(b-a+1)
    else:
        a = A[N//2]
        b = B[N//2]
        print(b-a+1)

=======
Suggestion 8

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = 0
    for i in range(N-1, -1, -1):
        A[i] += ans
        if A[i] % B[i] != 0:
            ans += B[i] - A[i] % B[i]
    print(ans)

=======
Suggestion 9

def solve(n, ab):
    #print(ab)
    #print(ab[0][0])
    #print(ab[0][1])
    #print(ab[1][0])
    #print(ab[1][1])
    #print(ab[2][0])
    #print(ab[2][1])
    #print(ab[3][0])
    #print(ab[3][1])
    #print(ab[4][0])
    #print(ab[4][1])
    #print(ab[5][0])
    #print(ab[5][1])
    #print(ab[6][0])
    #print(ab[6][1])
    #print(ab[7][0])
    #print(ab[7][1])
    #print(ab[8][0])
    #print(ab[8][1])
    #print(ab[9][0])
    #print(ab[9][1])
    #print(ab[10][0])
    #print(ab[10][1])
    #print(ab[11][0])
    #print(ab[11][1])
    #print(ab[12][0])
    #print(ab[12][1])
    #print(ab[13][0])
    #print(ab[13][1])
    #print(ab[14][0])
    #print(ab[14][1])
    #print(ab[15][0])
    #print(ab[15][1])
    #print(ab[16][0])
    #print(ab[16][1])
    #print(ab[17][0])
    #print(ab[17][1])
    #print(ab[18][0])
    #print(ab[18][1])
    #print(ab[19][0])
    #print(ab[19][1])
    #print(ab[20][0])
    #print(ab[20][1])
    #print(ab[21][0])
    #print(ab[21][1])
    #print(ab[22][0])
    #print(ab[22][1])
    #print(ab[23][0])
    #print(ab[23][1])
    #print(ab[24][0])
    #print(ab[24][1])
    #print(ab[25][0])
    #print(ab[25][1])
    #print(ab[26][0])
    #print(ab[26][1])
    #print(ab

=======
Suggestion 10

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)

    a_sum = sum(a)
    b_sum = sum(b)

    if a_sum < b_sum:
        print(0)
        return

    diff = []
    for i in range(n):
        diff.append(a[i] - b[i])

    diff.sort()
    diff.reverse()

    ans = 0
    for i in range(n):
        if a_sum >= b_sum:
            break
        a_sum -= diff[i]
        ans += 1

    print(ans)
