Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split()))[1:])
    like = set(A[0])
    for a in A[1:]:
        like = like & set(a)
    print(len(like))

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split()))[1:])
    ans = 0
    for i in range(1, m+1):
        for j in range(n):
            if i not in a[j]:
                break
        else:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(n)]
    cnt = [0] * (m + 1)
    for i in range(n):
        for j in range(1,a[i][0] + 1):
            cnt[a[i][j]] += 1
    ans = 0
    for i in range(m + 1):
        if cnt[i] == n:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    a = [0] * m
    for i in range(n):
        k, *aa = map(int, input().split())
        for j in aa:
            a[j-1] += 1
    print(a.count(n))

=======
Suggestion 5

def main():
    N,M = map(int, input().split())
    #print(N,M)

    A = [[0 for i in range(M)] for j in range(N)]
    #print(A)

    for i in range(N):
        A[i] = list(map(int, input().split()))
        #print(A[i])

    #print(A)

    #print(A[0][0])
    #print(A[0][1])
    #print(A[0][2])
    #print(A[0][3])

    #print(A[1][0])
    #print(A[1][1])
    #print(A[1][2])
    #print(A[1][3])

    #print(A[2][0])
    #print(A[2][1])
    #print(A[2][2])
    #print(A[2][3])

    #print(A[3][0])
    #print(A[3][1])
    #print(A[3][2])
    #print(A[3][3])

    #print(A[4][0])
    #print(A[4][1])
    #print(A[4][2])
    #print(A[4][3])

    #print(A[5][0])
    #print(A[5][1])
    #print(A[5][2])
    #print(A[5][3])

    #print(A[6][0])
    #print(A[6][1])
    #print(A[6][2])
    #print(A[6][3])

    #print(A[7][0])
    #print(A[7][1])
    #print(A[7][2])
    #print(A[7][3])

    #print(A[8][0])
    #print(A[8][1])
    #print(A[8][2])
    #print(A[8][3])

    #print(A[9][0])
    #print(A[9][1])
    #print(A[9][2])
    #print(A[9][3])

    #print(A[10][0])
    #print(A[10][1])
    #print(A[10][2])
    #print(A[10][3])

    #print(A[11][0])
    #print(A[11][1])
    #print(A[11][2])
    #print(A[

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    k = [0] * n
    a = [0] * n
    for i in range(n):
        k[i], *a[i] = map(int, input().split())
    s = set(a[0])
    for i in range(1, n):
        s &= set(a[i])
    print(len(s))

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = [0] * m
    for i in range(n):
        for j in range(1, a[i][0] + 1):
            ans[a[i][j] - 1] += 1
    print(ans.count(n))

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    #print("N:",N)
    #print("M:",M)
    #print("A:",A)
    #print("A[0][0]:",A[0][0])
    #print("A[0][1]:",A[0][1])
    #print("A[0][2]:",A[0][2])
    #print("A[1][0]:",A[1][0])
    #print("A[1][1]:",A[1][1])
    #print("A[1][2]:",A[1][2])
    #print("A[2][0]:",A[2][0])
    #print("A[2][1]:",A[2][1])
    #print("A[2][2]:",A[2][2])
    #print("A[3][0]:",A[3][0])
    #print("A[3][1]:",A[3][1])
    #print("A[3][2]:",A[3][2])
    #print("A[4][0]:",A[4][0])
    #print("A[4][1]:",A[4][1])
    #print("A[4][2]:",A[4][2])
    #print("A[5][0]:",A[5][0])
    #print("A[5][1]:",A[5][1])
    #print("A[5][2]:",A[5][2])
    #print("A[6][0]:",A[6][0])
    #print("A[6][1]:",A[6][1])
    #print("A[6][2]:",A[6][2])
    #print("A[7][0]:",A[7][0])
    #print("A[7][1]:",A[7][1])
    #print("A[7][2]:",A[7][2])
    #print("A[8][0]:",A[8][0])
    #print("A[8][1]:",A[8][

=======
Suggestion 9

def main():
    N,M = map(int,input().split())
    #print(N,M)
    result = 0
    like_list = []
    for i in range(N):
        like_list.append(list(map(int,input().split())))
    #print(like_list)
    for i in range(1,M+1):
        #print(i)
        for j in range(N):
            #print(like_list[j])
            if i in like_list[j][1:]:
                #print("OK")
                if j == N-1:
                    #print("OK")
                    result += 1
            else:
                break
    print(result)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split()))[1:])
    count = 0
    for i in range(1, M + 1):
        for j in range(N):
            if i in A[j]:
                if j == N - 1:
                    count += 1
                else:
                    continue
            else:
                break
    print(count)
