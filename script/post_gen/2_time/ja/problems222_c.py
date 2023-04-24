Synthesizing 8/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [input() for _ in range(2*N)]

    # 1 から 2N の番号がついた 2N 人でじゃんけん大会をします。
    # 大会は M ラウンドからなり、各ラウンドは、全ての人が 1 度ずつ参加するような 1 対 1 の N 試合からなります。
    # i=0,1,...,M について、i ラウンド目の終了時点での順位を次のように決めます。
    # i ラウンド目までの勝数が多い方が上位
    # i ラウンド目までの勝数が同じときは、番号が小さい方が上位
    # また、i=1,...,M について、i ラウンド目の各試合の組み合わせを次のように決めます。
    # 各 k=1,2,...,N について、i-1 ラウンド目終了時点の順位が 2k-1 位の人と 2k 位の人が試合をする
    # 各試合では、対戦する 2 人がそれぞれ 1 度だけ手を出し、勝ち・負け・引き分けのいずれかの結果が発生します。
    # 未来予知ができる高橋君は、人 i が j ラウンド目の試合で出す手が A_{i,j} であることを知っています。
    # A_{i,j} は G, C, P のいずれかであり、それぞれグー、チョキ、パーを表します。
    # M ラウンド目終了時

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = [input() for _ in range(2*N)]
    result = [0 for _ in range(2*N)]
    for i in range(M):
        for j in range(N):
            if A[2*j][i] == "G" and A[2*j+1][i] == "C":
                result[2*j] += 1
            elif A[2*j][i] == "C" and A[2*j+1][i] == "P":
                result[2*j] += 1
            elif A[2*j][i] == "P" and A[2*j+1][i] == "G":
                result[2*j] += 1
            elif A[2*j][i] == "G" and A[2*j+1][i] == "P":
                result[2*j+1] += 1
            elif A[2*j][i] == "C" and A[2*j+1][i] == "G":
                result[2*j+1] += 1
            elif A[2*j][i] == "P" and A[2*j+1][i] == "C":
                result[2*j+1] += 1
        rank = sorted(result, reverse=True)
        for j in range(2*N):
            result[j] = rank.index(result[j]) + 1
    for i in range(2*N):
        print(result.index(i+1)+1)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = [input() for _ in range(2*N)]
    rank = list(range(2*N))
    for j in range(M):
        next_rank = [-1] * (2*N)
        for i in range(N):
            a = rank[2*i]
            b = rank[2*i+1]
            if (A[a][j] == A[b][j]):
                next_rank[2*i] = a
                next_rank[2*i+1] = b
            elif (A[a][j] == 'G' and A[b][j] == 'C') or (A[a][j] == 'C' and A[b][j] == 'P') or (A[a][j] == 'P' and A[b][j] == 'G'):
                next_rank[2*i] = a
                next_rank[2*i+1] = b
            else:
                next_rank[2*i] = b
                next_rank[2*i+1] = a
        rank = next_rank
    for i in range(2*N):
        print(rank.index(i)+1)

=======
Suggestion 4

def main():
    import sys
    input = sys.stdin.readline
    N, M = map(int, input().split())
    A = [input().rstrip() for _ in range(2*N)]
    #print(N,M)
    #print(A)

    # 1 から 2N の番号がついた 2N 人でじゃんけん大会をします。
    # 大会は M ラウンドからなり、各ラウンドは、全ての人が 1 度ずつ参加するような 1 対 1 の N 試合からなります。
    # i=0,1,...,M について、i ラウンド目の終了時点での順位を次のように決めます。
    # i ラウンド目までの勝数が多い方が上位
    # i ラウンド目までの勝数が同じときは、番号が小さい方が上位
    # また、i=1,...,M について、i ラウンド目の各試合の組み合わせを次のように決めます。
    # 各 k=1,2,...,N について、i-1 ラウンド目終了時点の順位が 2k-1 位の人と 2k 位の人が試合をする
    # 各試合では、対戦する 2 人がそれぞれ 1 度だけ手を出し、勝ち・負け・引き分けのいずれかの結果が発生します。
    # 未来予知ができる高橋君は、人 i が j ラウンド目の試合で出す手が A_{i,j} であることを知っています。
    # A_{i,j} は G, C, P のいずれかであり、それぞれグー

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = [input() for _ in range(2*N)]
    #print(N, M)
    #print(A)
    #print(A[0][0])
    #print(A[1][0])
    #print(A[2][0])
    #print(A[3][0])
    #print(A[4][0])
    #print(A[5][0])
    #print(A[0][1])
    #print(A[1][1])
    #print(A[2][1])
    #print(A[3][1])
    #print(A[4][1])
    #print(A[5][1])
    #print(A[0][2])
    #print(A[1][2])
    #print(A[2][2])
    #print(A[3][2])
    #print(A[4][2])
    #print(A[5][2])
    #print(A[0][3])
    #print(A[1][3])
    #print(A[2][3])
    #print(A[3][3])
    #print(A[4][3])
    #print(A[5][3])
    #print(A[0][4])
    #print(A[1][4])
    #print(A[2][4])
    #print(A[3][4])
    #print(A[4][4])
    #print(A[5][4])
    #print(A[0][5])
    #print(A[1][5])
    #print(A[2][5])
    #print(A[3][5])
    #print(A[4][5])
    #print(A[5][5])
    #print(A[0][6])
    #print(A[1][6])
    #print(A[2][6])
    #print(A[3][6])
    #print(A[4][6])
    #print(A[5][6])
    #print(A[0][7])
    #print(A[1][7])
    #print(A[2][7])
    #print(A[3][7])
    #print(A[4][7])
    #print(A[5][7])
    #print(A[0][8])
    #print(A[1][8])
    #print(A[2][8])

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = [input() for i in range(2*N)]
    win = [0]*2*N
    next = [i for i in range(2*N)]
    for i in range(M):
        for j in range(N):
            if A[next[2*j]][i] == A[next[2*j+1]][i]:
                pass
            elif A[next[2*j]][i] == 'G' and A[next[2*j+1]][i] == 'C':
                win[next[2*j]] += 1
            elif A[next[2*j]][i] == 'C' and A[next[2*j+1]][i] == 'P':
                win[next[2*j]] += 1
            elif A[next[2*j]][i] == 'P' and A[next[2*j+1]][i] == 'G':
                win[next[2*j]] += 1
            else:
                win[next[2*j+1]] += 1
        next = sorted(next, key=lambda x: (-win[x], x))
        #print(next)
    for i in next:
        print(i+1)

=======
Suggestion 7

def main():
    N,M = map(int,input().split())
    A = []
    for i in range(2*N):
        A.append(input())
    #print(A)
    #print(N,M)
    #print(len(A))
    #print(A[0][0])
    #print(A[1][0])
    #print(A[2][0])
    #print(A[3][0])
    #print(A[4][0])
    #print(A[5][0])
    #print(A[6][0])
    #print(A[7][0])

    #print(A[0][1])
    #print(A[1][1])
    #print(A[2][1])
    #print(A[3][1])
    #print(A[4][1])
    #print(A[5][1])
    #print(A[6][1])
    #print(A[7][1])

    #print(A[0][2])
    #print(A[1][2])
    #print(A[2][2])
    #print(A[3][2])
    #print(A[4][2])
    #print(A[5][2])
    #print(A[6][2])
    #print(A[7][2])

    #print(A[0][3])
    #print(A[1][3])
    #print(A[2][3])
    #print(A[3][3])
    #print(A[4][3])
    #print(A[5][3])
    #print(A[6][3])
    #print(A[7][3])

    #print(A[0][4])
    #print(A[1][4])
    #print(A[2][4])
    #print(A[3][4])
    #print(A[4][4])
    #print(A[5][4])
    #print(A[6][4])
    #print(A[7][4])

    #print(A[0][5])
    #print(A[1][5])
    #print(A[2][5])
    #print(A[3][5])
    #print(A[4][5])
    #print(A[5][5])
    #print(A[6][5])
    #print(A[7][5])

    #print(A[0][6])
    #print(A[1][6])
    #print

=======
Suggestion 8

def solve():
    N, M = map(int, input().split())
    A = [input() for _ in range(2*N)]

    # 各ラウンドの勝敗を記録
    # 1ラウンド目：[0,0,0,0]
    # 2ラウンド目：[0,0,0,0]
    # 3ラウンド目：[0,0,0,0]
    win = [ [0]*2*N for _ in range(M) ]

    # 各ラウンドの順位を記録
    # 1ラウンド目：[0,1,2,3]
    # 2ラウンド目：[0,1,2,3]
    # 3ラウンド目：[0,1,2,3]
    rank = [ [i for i in range(2*N)] for _ in range(M) ]

    # 1ラウンド目の勝敗を記録
    for i in range(2*N):
        for j in range(M):
            if A[i][j] == "G":
                if A[i+1][j] == "C":
                    win[j][i] = 1
                elif A[i+1][j] == "P":
                    win[j][i+1] = 1
            elif A[i][j] == "C":
                if A[i+1][j] == "P":
                    win[j][i] = 1
                elif A[i+1][j] == "G":
                    win[j][i+1] = 1
            elif A[i][j] == "P":
                if A[i+1][j] == "G":
                    win[j][i] = 1
                elif A[i+1][j] == "C":
                    win[j][i+1] = 1

    # 2ラウンド目以降の勝敗を記録
    for j in range(1,M):
        # 1位と2位の勝敗を記録
        for i in range(0,2*N,2):
            if win[j-1][rank[j-1][
