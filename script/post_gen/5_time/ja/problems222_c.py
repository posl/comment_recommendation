Synthesizing 10/10 solutions

=======
Suggestion 1

def janken(a, b):
    if a == b:
        return 0
    elif a == "G":
        if b == "C":
            return 1
        else:
            return -1
    elif a == "C":
        if b == "P":
            return 1
        else:
            return -1
    else:
        if b == "G":
            return 1
        else:
            return -1

=======
Suggestion 2

def judge(a,b):
    if a == b:
        return 0
    elif a == "G":
        if b == "C":
            return 1
        elif b == "P":
            return -1
    elif a == "C":
        if b == "P":
            return 1
        elif b == "G":
            return -1
    elif a == "P":
        if b == "G":
            return 1
        elif b == "C":
            return -1

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    a = [list(input()) for _ in range(2 * n)]

    rank = [[i, 0] for i in range(2 * n)]

    for i in range(m):
        for j in range(n):
            hand1 = a[rank[2 * j][0]][i]
            hand2 = a[rank[2 * j + 1][0]][i]
            if hand1 == hand2:
                continue
            elif hand1 == 'G':
                if hand2 == 'C':
                    rank[2 * j][1] += 1
                else:
                    rank[2 * j + 1][1] += 1
            elif hand1 == 'C':
                if hand2 == 'P':
                    rank[2 * j][1] += 1
                else:
                    rank[2 * j + 1][1] += 1
            else:
                if hand2 == 'G':
                    rank[2 * j][1] += 1
                else:
                    rank[2 * j + 1][1] += 1
        rank.sort(key=lambda x: (-x[1], x[0]))
    for i in range(2 * n):
        print(rank[i][0] + 1)

=======
Suggestion 4

def janken(a,b):
    if a == b:
        return 0
    elif a == 'G':
        if b == 'C':
            return 1
        else:
            return -1
    elif a == 'C':
        if b == 'P':
            return 1
        else:
            return -1
    elif a == 'P':
        if b == 'G':
            return 1
        else:
            return -1

N, M = map(int, input().split())
A = [input() for _ in range(2*N)]
rank = [[i,0] for i in range(2*N)]
for i in range(M):
    for j in range(N):
        a = rank[2*j][0]
        b = rank[2*j+1][0]
        result = janken(A[a][i], A[b][i])
        if result == 1:
            rank[2*j][1] -= 1
        elif result == -1:
            rank[2*j+1][1] -= 1
    rank.sort(key=lambda x:(x[1], x[0]))
for i in range(2*N):
    print(rank[i][0]+1)

=======
Suggestion 5

def janken(a, b):
    if a == b:
        return 0
    if a == "G":
        if b == "C":
            return 1
        if b == "P":
            return -1
    if a == "C":
        if b == "P":
            return 1
        if b == "G":
            return -1
    if a == "P":
        if b == "G":
            return 1
        if b == "C":
            return -1

=======
Suggestion 6

def check(a,b):
    if a == "G" and b == "C":
        return True
    elif a == "C" and b == "P":
        return True
    elif a == "P" and b == "G":
        return True
    else:
        return False

n,m = map(int,input().split())
a = []
for i in range(2*n):
    a.append(input())
rank = []
for i in range(2*n):
    rank.append([0,i+1])
for i in range(m):
    for j in range(n):
        if check(a[rank[2*j][1]-1][i],a[rank[2*j+1][1]-1][i]):
            rank[2*j][0] -= 1
        elif check(a[rank[2*j+1][1]-1][i],a[rank[2*j][1]-1][i]):
            rank[2*j+1][0] -= 1
rank.sort()
for i in range(2*n):
    print(rank[i][1])

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = [input() for _ in range(2*N)]
    rank = [(0, i) for i in range(2*N)]

    for i in range(M):
        rank.sort()
        new_rank = []
        for j in range(0, 2*N, 2):
            p1 = rank[j][1]
            p2 = rank[j+1][1]
            if A[p1][i] == A[p2][i]:
                new_rank.append(rank[j])
                new_rank.append(rank[j+1])
            elif A[p1][i] == 'G' and A[p2][i] == 'C':
                new_rank.append((rank[j][0]-1, rank[j][1]))
                new_rank.append((rank[j+1][0]+1, rank[j+1][1]))
            elif A[p1][i] == 'C' and A[p2][i] == 'P':
                new_rank.append((rank[j][0]-1, rank[j][1]))
                new_rank.append((rank[j+1][0]+1, rank[j+1][1]))
            elif A[p1][i] == 'P' and A[p2][i] == 'G':
                new_rank.append((rank[j][0]-1, rank[j][1]))
                new_rank.append((rank[j+1][0]+1, rank[j+1][1]))
            else:
                new_rank.append((rank[j][0]+1, rank[j][1]))
                new_rank.append((rank[j+1][0]-1, rank[j+1][1]))
        rank = new_rank

    rank.sort()
    for r in rank:
        print(r[1]+1)

=======
Suggestion 8

def main():
    N,M = map(int,input().split())
    A = [input() for i in range(2*N)]
    #print(A)
    #print(A[0])
    #print(A[0][0])
    #print(A[0][1])
    #print(A[1][0])
    #print(A[1][1])
    #print(A[2][0])
    #print(A[2][1])
    #print(A[3][0])
    #print(A[3][1])
    #print(A[4][0])
    #print(A[4][1])
    #print(A[5][0])
    #print(A[5][1])
    #print(A[6][0])
    #print(A[6][1])
    #print(A[7][0])
    #print(A[7][1])
    #print(A[8][0])
    #print(A[8][1])
    #print(A[9][0])
    #print(A[9][1])
    #print(A[10][0])
    #print(A[10][1])
    #print(A[11][0])
    #print(A[11][1])
    #print(A[12][0])
    #print(A[12][1])
    #print(A[13][0])
    #print(A[13][1])
    #print(A[14][0])
    #print(A[14][1])
    #print(A[15][0])
    #print(A[15][1])
    #print(A[16][0])
    #print(A[16][1])
    #print(A[17][0])
    #print(A[17][1])
    #print(A[18][0])
    #print(A[18][1])
    #print(A[19][0])
    #print(A[19][1])
    #print(A[20][0])
    #print(A[20][1])
    #print(A[21][0])
    #print(A[21][1])
    #print(A[22][0])
    #print(A[22][1])
    #print(A[23][0])
    #print(A[23][1])
    #print(A[24][0])
    #print(A[24][1])
    #print(A[25][0])
    #print

=======
Suggestion 9

def janken(a, b):
    if a == b:
        return 0
    elif (a == "G" and b == "C") or (a == "C" and b == "P") or (a == "P" and b == "G"):
        return 1
    elif (a == "G" and b == "P") or (a == "C" and b == "G") or (a == "P" and b == "C"):
        return -1

=======
Suggestion 10

def main():
    N,M = map(int,input().split())
    A = []
    for i in range(2*N):
        A.append(input())
    rank = [[0,i] for i in range(2*N)]
    for i in range(M):
        for j in range(N):
            a = rank[2*j][1]
            b = rank[2*j+1][1]
            if A[a][i] == A[b][i]:
                continue
            elif A[a][i] == "G":
                if A[b][i] == "C":
                    rank[2*j][0] -= 1
                else:
                    rank[2*j+1][0] -= 1
            elif A[a][i] == "C":
                if A[b][i] == "P":
                    rank[2*j][0] -= 1
                else:
                    rank[2*j+1][0] -= 1
            else:
                if A[b][i] == "G":
                    rank[2*j][0] -= 1
                else:
                    rank[2*j+1][0] -= 1
        rank = sorted(rank)
    for i in range(2*N):
        print(rank[i][1]+1)
