Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [input() for _ in range(2*N)]
    A = [[A[i][j] for i in range(2*N)] for j in range(M)]
    A = [[0 for _ in range(2*N)] for _ in range(M)] + A
    for i in range(M-1, -1, -1):
        for j in range(N):
            a = A[i][2*j]
            b = A[i][2*j+1]
            if (a == 'G' and b == 'C') or (a == 'C' and b == 'P') or (a == 'P' and b == 'G'):
                A[i-1][2*j] += 1
            elif (a == 'C' and b == 'G') or (a == 'P' and b == 'C') or (a == 'G' and b == 'P'):
                A[i-1][2*j+1] += 1
            else:
                A[i-1][2*j] += 0.5
                A[i-1][2*j+1] += 0.5
    A = A[0]
    A = [(A[i], i+1) for i in range(2*N)]
    A.sort()
    A = [x[1] for x in A]
    A.reverse()
    for i in range(2*N):
        print(A[i])

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = [input() for i in range(2 * N)]
    rank = [i for i in range(1, 2 * N + 1)]
    for i in range(M):
        win = [0 for i in range(2 * N)]
        for j in range(N):
            if A[rank[2 * j] - 1][i] == A[rank[2 * j + 1] - 1][i]:
                win[rank[2 * j] - 1] += 1
                win[rank[2 * j + 1] - 1] += 1
            elif (A[rank[2 * j] - 1][i] == 'G' and A[rank[2 * j + 1] - 1][i] == 'C') or (A[rank[2 * j] - 1][i] == 'C' and A[rank[2 * j + 1] - 1][i] == 'P') or (A[rank[2 * j] - 1][i] == 'P' and A[rank[2 * j + 1] - 1][i] == 'G'):
                win[rank[2 * j] - 1] += 3
            else:
                win[rank[2 * j + 1] - 1] += 3
        rank = sorted(range(2 * N), key=lambda x: (-win[x], x))
        rank = [i + 1 for i in rank]
    for i in rank:
        print(i)

=======
Suggestion 3

def get_winner(a,b):
    if (a == "G" and b == "C") or (a == "C" and b == "P") or (a == "P" and b == "G"):
        return 0
    elif (a == "G" and b == "P") or (a == "C" and b == "G") or (a == "P" and b == "C"):
        return 1
    elif a == b:
        return 2

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = [input() for _ in range(2*N)]

    player = [i+1 for i in range(2*N)]
    for i in range(M):
        for j in range(N):
            if A[player[2*j]-1][i] == A[player[2*j+1]-1][i]:
                continue
            elif A[player[2*j]-1][i] == 'G' and A[player[2*j+1]-1][i] == 'C':
                player[2*j], player[2*j+1] = player[2*j+1], player[2*j]
            elif A[player[2*j]-1][i] == 'C' and A[player[2*j+1]-1][i] == 'P':
                player[2*j], player[2*j+1] = player[2*j+1], player[2*j]
            elif A[player[2*j]-1][i] == 'P' and A[player[2*j+1]-1][i] == 'G':
                player[2*j], player[2*j+1] = player[2*j+1], player[2*j]

    for i in range(2*N):
        print(player[i])

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = [input() for _ in range(2*n)]
    for i in range(m):
        win = [0 for _ in range(2*n)]
        for j in range(n):
            if a[2*j][i] == a[2*j+1][i]:
                win[2*j] += 1
                win[2*j+1] += 1
            elif a[2*j][i] == "G" and a[2*j+1][i] == "C":
                win[2*j] += 3
            elif a[2*j][i] == "C" and a[2*j+1][i] == "P":
                win[2*j] += 3
            elif a[2*j][i] == "P" and a[2*j+1][i] == "G":
                win[2*j] += 3
            else:
                win[2*j+1] += 3
        a = [a[i] for i in sorted(range(2*n), key=lambda x: (-win[x], x))]
    for i in range(2*n):
        print(a[i])

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = [input() for _ in range(2*N)]

    for i in range(M):
        win = [-1] * (2*N)
        for j in range(N):
            a = 2*j
            b = 2*j+1
            if A[a][i] == A[b][i]:
                win[a] = 0
                win[b] = 0
            elif A[a][i] == 'G' and A[b][i] == 'C':
                win[a] = 1
                win[b] = 0
            elif A[a][i] == 'C' and A[b][i] == 'P':
                win[a] = 1
                win[b] = 0
            elif A[a][i] == 'P' and A[b][i] == 'G':
                win[a] = 1
                win[b] = 0
            else:
                win[a] = 0
                win[b] = 1
        for j in range(2*N):
            win[j] += win.count(1)
        A = [A[i] for i in sorted(range(2*N), key=lambda x: win[x], reverse=True)]
    for i in range(2*N):
        print(i+1)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = [input() for _ in range(2*N)]
    #print(N, M, A)
    rank = [[0, i+1] for i in range(2*N)]
    for i in range(M):
        for j in range(N):
            p1 = rank[2*j][1]
            p2 = rank[2*j+1][1]
            if A[p1-1][i] == A[p2-1][i]:
                continue
            elif A[p1-1][i] == 'G' and A[p2-1][i] == 'C':
                rank[2*j][0] += 1
            elif A[p1-1][i] == 'G' and A[p2-1][i] == 'P':
                rank[2*j+1][0] += 1
            elif A[p1-1][i] == 'C' and A[p2-1][i] == 'G':
                rank[2*j+1][0] += 1
            elif A[p1-1][i] == 'C' and A[p2-1][i] == 'P':
                rank[2*j][0] += 1
            elif A[p1-1][i] == 'P' and A[p2-1][i] == 'G':
                rank[2*j][0] += 1
            elif A[p1-1][i] == 'P' and A[p2-1][i] == 'C':
                rank[2*j+1][0] += 1
        rank.sort(key=lambda x: (-x[0], x[1]))
        #print(rank)
    for r in rank:
        print(r[1])

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = [input() for _ in range(2*N)]
    #print(N, M)
    #print(A)

    #ID = [i for i in range(1, 2*N+1)]

    #print(ID)
    #print()

    #print("===== start =====")
    for i in range(M):
        #print("===== round {} =====".format(i+1))
        #print(ID)
        #print()
        ID = [i for i in range(1, 2*N+1)]
        for j in range(N):
            #print("===== match {} =====".format(j+1))
            #print(ID)
            #print()
            if A[ID[2*j]-1][i] == A[ID[2*j+1]-1][i]:
                continue
            elif A[ID[2*j]-1][i] == "G":
                if A[ID[2*j+1]-1][i] == "C":
                    ID[2*j], ID[2*j+1] = ID[2*j+1], ID[2*j]
                else:
                    pass
            elif A[ID[2*j]-1][i] == "C":
                if A[ID[2*j+1]-1][i] == "P":
                    ID[2*j], ID[2*j+1] = ID[2*j+1], ID[2*j]
                else:
                    pass
            elif A[ID[2*j]-1][i] == "P":
                if A[ID[2*j+1]-1][i] == "G":
                    ID[2*j], ID[2*j+1] = ID[2*j+1], ID[2*j]
                else:
                    pass
            else:
                pass
        #print("===== end =====")
        #print(ID)
        #print()
    #print("===== finish =====")
    #print(ID)
    #print()
    for i in range(2*N):
        print(ID[i])

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    A = [input() for _ in range(2*N)]
    #print(A)
    #print(N,M)
    R = [i for i in range(1,2*N+1)]
    #print(R)
    for i in range(M):
        #print("Round",i+1)
        for j in range(N):
            #print("Match",j+1)
            #print(R)
            p1 = R[2*j]
            p2 = R[2*j+1]
            if A[p1-1][i] == "G":
                if A[p2-1][i] == "C":
                    R[2*j] = p1
                    R[2*j+1] = p2
                elif A[p2-1][i] == "P":
                    R[2*j] = p2
                    R[2*j+1] = p1
                else:
                    R[2*j] = p1
                    R[2*j+1] = p2
            elif A[p1-1][i] == "C":
                if A[p2-1][i] == "P":
                    R[2*j] = p1
                    R[2*j+1] = p2
                elif A[p2-1][i] == "G":
                    R[2*j] = p2
                    R[2*j+1] = p1
                else:
                    R[2*j] = p1
                    R[2*j+1] = p2
            elif A[p1-1][i] == "P":
                if A[p2-1][i] == "G":
                    R[2*j] = p1
                    R[2*j+1] = p2
                elif A[p2-1][i] == "C":
                    R[2*j] = p2
                    R[2*j+1] = p1
                else:
                    R[2*j] = p1
                    R[2*j+1] = p2
        #print(R)
    for k in range(2*N):
        print(R[k])

=======
Suggestion 10

def main():
    N, M = map(int, input().split())

    # 1回目のマッチング
    match = []
    for i in range(1, 2*N, 2):
        match.append([i, i+1])

    # 2回目以降のマッチング
    for _ in range(M):
        A = input()
        match_new = []
        for i in range(N):
            if A[i] == 'G':
                if A[i+N] == 'P':
                    match_new.append(match[i][1])
                    match_new.append(match[i][0])
                elif A[i+N] == 'C':
                    match_new.append(match[i][0])
                    match_new.append(match[i][1])
                else:
                    match_new.append(match[i][0])
                    match_new.append(match[i][1])
            elif A[i] == 'C':
                if A[i+N] == 'P':
                    match_new.append(match[i][0])
                    match_new.append(match[i][1])
                elif A[i+N] == 'G':
                    match_new.append(match[i][1])
                    match_new.append(match[i][0])
                else:
                    match_new.append(match[i][0])
                    match_new.append(match[i][1])
            else:
                if A[i+N] == 'G':
                    match_new.append(match[i][0])
                    match_new.append(match[i][1])
                elif A[i+N] == 'C':
                    match_new.append(match[i][1])
                    match_new.append(match[i][0])
                else:
                    match_new.append(match[i][0])
                    match_new.append(match[i][1])
        match = match_new

    for i in range(2*N):
        print(match[i])
