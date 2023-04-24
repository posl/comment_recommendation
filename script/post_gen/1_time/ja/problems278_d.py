Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    for i in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            A = [query[1]]*N
        elif query[0] == 2:
            A[query[1]-1] += query[2]
        else:
            print(A[query[1]-1])

=======
Suggestion 2

def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    ans = []
    # 1
    for q in query:
        if q[0] == 1:
            x = q[1]
            for i in range(N):
                A[i] = x
        # 2
        elif q[0] == 2:
            A[q[1]-1] += q[2]
        # 3
        else:
            ans.append(A[q[1]-1])
    for a in ans:
        print(a)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    x = 0
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            x = query[1]
        elif query[0] == 2:
            a[query[1] - 1] += query[2] - x
        else:
            print(a[query[1] - 1] + x)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    for i in range(Q):
        if query[i][0] == 1:
            A = [query[i][1]] * N
        elif query[i][0] == 2:
            A[query[i][1]-1] += query[i][2]
        else:
            print(A[query[i][1]-1])

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int,input().split()))
    q = int(input())
    query = []
    for i in range(q):
        query.append(list(map(int,input().split())))
    ans = []
    for i in range(q):
        if query[i][0] == 1:
            a = [query[i][1]]*n
        elif query[i][0] == 2:
            a[query[i][1]-1] += query[i][2]
        elif query[i][0] == 3:
            ans.append(a[query[i][1]-1])
    for i in range(len(ans)):
        print(ans[i])

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    #print(N)
    #print(A)
    #print(Q)
    #print(query)
    #print(query[0][0])
    #print(query[0][1])
    #print(query[0][2])
    #print(query[1][0])
    #print(query[1][1])
    #print(query[1][2])
    #print(query[2][0])
    #print(query[2][1])
    #print(query[3][0])
    #print(query[3][1])
    #print(query[3][2])
    #print(query[4][0])
    #print(query[4][1])
    #print(query[4][2])
    #print(query[5][0])
    #print(query[5][1])
    #print(query[5][2])
    #print(query[6][0])
    #print(query[6][1])
    #print(query[7][0])
    #print(query[7][1])
    #print(query[8][0])
    #print(query[8][1])
    #print(query[9][0])
    #print(query[9][1])
    #print(query[10][0])
    #print(query[10][1])
    #print(query[11][0])
    #print(query[11][1])
    #print(query[12][0])
    #print(query[12][1])
    #print(query[13][0])
    #print(query[13][1])
    #print(query[14][0])
    #print(query[14][1])
    #print(query[15][0])
    #print(query[15][1])
    #print(query[16][0])
    #print(query[16][1])
    #print(query[17][0])
    #print(query[17][1])
    #print(query[18][0])
    #print(query[18][1])
    #print(query[19][0])
    #print(query[19][1])
    #print(query[20][0])
    #print(query[20][1])
    #print(query[21][0])
    #print(query[

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]

    # 累積和の配列
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]

    # 1回目のクエリで変更される値
    # 2回目以降のクエリで変更される値
    # 1回目のクエリで変更される値を2回目以降のクエリで変更される値に加算する
    # 2回目以降のクエリで変更される値を1回目のクエリで変更される値に加算する
    # 1回目のクエリで変更される値を2回目以降のクエリで変更される値に加算する
    # 2回目以降のクエリで変更される値を1回目のクエリで変更される値に加算する
    # 1回目のクエリで変更される値を2回目以降のクエリで変更される値に加算する
    # 2回目以降のクエリで変更される値を1回目のクエリで変更される値に加算する
    # 1回目のクエリで変更される値を2回目以降のクエリで変更される値に加算する
    # 2回目以降のクエリで変更される値を1回目のクエリで変更される値に加算する
    # 1回目のクエリで変更される値を2回目以降のクエリで変更

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    que = [list(map(int, input().split())) for _ in range(q)]
    add = [0] * n
    for i in range(q):
        if que[i][0] == 1:
            add = [que[i][1]] * n
        elif que[i][0] == 2:
            a[que[i][1] - 1] += que[i][2]
        else:
            print(a[que[i][1] - 1] + add[que[i][1] - 1])

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    #print(N)
    #print(A)
    #print(Q)
    #A = [0] * N
    #print(A)
    #print(len(A))
    #print(A[0])
    #print(A[1])
    #print(A[2])
    #print(A[3])
    #print(A[4])
    #print(A[5])
    #print(A[6])
    #print(A[7])
    #print(A[8])
    #print(A[9])
    #print(A[10])
    #print(A[11])
    #print(A[12])
    #print(A[13])
    #print(A[14])
    #print(A[15])
    #print(A[16])
    #print(A[17])
    #print(A[18])
    #print(A[19])
    #print(A[20])
    #print(A[21])
    #print(A[22])
    #print(A[23])
    #print(A[24])
    #print(A[25])
    #print(A[26])
    #print(A[27])
    #print(A[28])
    #print(A[29])
    #print(A[30])
    #print(A[31])
    #print(A[32])
    #print(A[33])
    #print(A[34])
    #print(A[35])
    #print(A[36])
    #print(A[37])
    #print(A[38])
    #print(A[39])
    #print(A[40])
    #print(A[41])
    #print(A[42])
    #print(A[43])
    #print(A[44])
    #print(A[45])
    #print(A[46])
    #print(A[47])
    #print(A[48])
    #print(A[49])
    #print(A[50])
    #print(A[51])
    #print(A[52])
    #print(A[53])
    #print(A[54])
    #print(A[55])
    #print(A[56])
    #print(A[57])
    #print(A[58])
    #print(A[59])
    #print(A[60])
    #print(A[61])
    #print(A[
