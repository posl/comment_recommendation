Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N,M = map(int,input().split())
    A = []
    for i in range(2*N):
        A.append(input())
    rank = [[i+1,0] for i in range(2*N)]
    for i in range(M):
        for j in range(0,2*N,2):
            if A[rank[j][0]-1][i] == A[rank[j+1][0]-1][i]:
                continue
            elif A[rank[j][0]-1][i] == 'G' and A[rank[j+1][0]-1][i] == 'C':
                rank[j][1] -= 1
            elif A[rank[j][0]-1][i] == 'C' and A[rank[j+1][0]-1][i] == 'P':
                rank[j][1] -= 1
            elif A[rank[j][0]-1][i] == 'P' and A[rank[j+1][0]-1][i] == 'G':
                rank[j][1] -= 1
            else:
                rank[j+1][1] -= 1
        rank.sort(key=lambda x:(x[1],x[0]))
    for i in range(2*N):
        print(rank[i][0])

=======
Suggestion 2

def main():
    N,M = map(int,input().split())
    A = [list(input()) for _ in range(2*N)]
    rank = [[i,0] for i in range(2*N)]
    for i in range(M):
        for j in range(N):
            p1 = rank[2*j][0]
            p2 = rank[2*j+1][0]
            if A[p1][i] == A[p2][i]:
                continue
            elif A[p1][i] == 'G':
                if A[p2][i] == 'C':
                    rank[2*j][1] -= 1
                else:
                    rank[2*j+1][1] -= 1
            elif A[p1][i] == 'C':
                if A[p2][i] == 'P':
                    rank[2*j][1] -= 1
                else:
                    rank[2*j+1][1] -= 1
            else:
                if A[p2][i] == 'G':
                    rank[2*j][1] -= 1
                else:
                    rank[2*j+1][1] -= 1
        rank.sort(key=lambda x:(x[1],x[0]))
    for i in range(2*N):
        print(rank[i][0]+1)

=======
Suggestion 3

def gcp(a, b):
    if a == b:
        return 0
    elif a == 'G' and b == 'C':
        return 1
    elif a == 'C' and b == 'P':
        return 1
    elif a == 'P' and b == 'G':
        return 1
    else:
        return -1

=======
Suggestion 4

def judge(player1,player2):
    if player1 == player2:
        return 0
    elif player1 == 'G' and player2 == 'C':
        return 1
    elif player1 == 'C' and player2 == 'P':
        return 1
    elif player1 == 'P' and player2 == 'G':
        return 1
    else:
        return 2

=======
Suggestion 5

def solve():
    n,m = map(int,input().split())
    a = []
    for _ in range(2*n):
        a.append(list(input()))
    rank = [i for i in range(2*n)]
    for i in range(m):
        for j in range(n):
            x = rank[2*j]
            y = rank[2*j+1]
            if a[x][i] == a[y][i]:
                continue
            elif a[x][i] == 'G' and a[y][i] == 'C':
                rank[2*j] = y
                rank[2*j+1] = x
            elif a[x][i] == 'C' and a[y][i] == 'P':
                rank[2*j] = y
                rank[2*j+1] = x
            elif a[x][i] == 'P' and a[y][i] == 'G':
                rank[2*j] = y
                rank[2*j+1] = x
    for i in range(2*n):
        print(rank[i]+1)

=======
Suggestion 6

def check_winner(a, b):
    if a == 'G' and b == 'C':
        return True
    elif a == 'C' and b == 'P':
        return True
    elif a == 'P' and b == 'G':
        return True
    else:
        return False

=======
Suggestion 7

def judge(a,b):
    if a == b:
        return 0
    elif (a == "G" and b == "C") or (a == "C" and b == "P") or (a == "P" and b == "G"):
        return 1
    else:
        return -1

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = [input() for _ in range(2 * N)]
    rank = [[i + 1, 0] for i in range(2 * N)]
    for i in range(M):
        for j in range(N):
            k = 2 * j
            if (A[rank[k][0] - 1][i] == "G" and A[rank[k + 1][0] - 1][i] == "C") or (A[rank[k][0] - 1][i] == "C" and A[rank[k + 1][0] - 1][i] == "P") or (A[rank[k][0] - 1][i] == "P" and A[rank[k + 1][0] - 1][i] == "G"):
                rank[k][1] += 1
            elif (A[rank[k][0] - 1][i] == "C" and A[rank[k + 1][0] - 1][i] == "G") or (A[rank[k][0] - 1][i] == "P" and A[rank[k + 1][0] - 1][i] == "C") or (A[rank[k][0] - 1][i] == "G" and A[rank[k + 1][0] - 1][i] == "P"):
                rank[k + 1][1] += 1
        rank.sort(key=lambda x: x[1], reverse=True)
    for i in range(2 * N):
        print(rank[i][0])

=======
Suggestion 9

def getRanking(N, M, A):
    #print(N, M, A)
    #print("A[1][1]", A[1][1])
    #print("A[2][1]", A[2][1])
    #print("A[3][1]", A[3][1])
    #print("A[4][1]", A[4][1])
    #print("A[5][1]", A[5][1])
    #print("A[6][1]", A[6][1])
    #print("A[7][1]", A[7][1])
    #print("A[8][1]", A[8][1])
    #print("A[9][1]", A[9][1])
    #print("A[10][1]", A[10][1])
    #print("A[11][1]", A[11][1])
    #print("A[12][1]", A[12][1])
    #print("A[13][1]", A[13][1])
    #print("A[14][1]", A[14][1])
    #print("A[15][1]", A[15][1])
    #print("A[16][1]", A[16][1])
    #print("A[17][1]", A[17][1])
    #print("A[18][1]", A[18][1])
    #print("A[19][1]", A[19][1])
    #print("A[20][1]", A[20][1])
    #print("A[21][1]", A[21][1])
    #print("A[22][1]", A[22][1])
    #print("A[23][1]", A[23][1])
    #print("A[24][1]", A[24][1])
    #print("A[25][1]", A[25][1])
    #print("A[26][1]", A[26][1])
    #print("A[27][1]", A[27][1])
    #print("A[28][1]", A[28][1])
    #print("A[29][1]", A[29][1])
    #print("A[30][1]", A[30][1])
    #

=======
Suggestion 10

def RPS(i,j):
    if i == 'G':
        if j == 'G':
            return 0
        elif j == 'C':
            return 1
        elif j == 'P':
            return -1
    elif i == 'C':
        if j == 'G':
            return -1
        elif j == 'C':
            return 0
        elif j == 'P':
            return 1
    elif i == 'P':
        if j == 'G':
            return 1
        elif j == 'C':
            return -1
        elif j == 'P':
            return 0
