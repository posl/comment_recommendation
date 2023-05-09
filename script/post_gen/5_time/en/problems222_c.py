Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [input() for _ in range(2*N)]
    rank = []
    for i in range(2*N):
        rank.append((0, i+1))
    for i in range(M):
        for j in range(N):
            p1 = rank[2*j]
            p2 = rank[2*j+1]
            if A[p1[1]-1][i] == A[p2[1]-1][i]:
                continue
            elif A[p1[1]-1][i] == 'G' and A[p2[1]-1][i] == 'C':
                rank[2*j] = (p1[0]+1, p1[1])
            elif A[p1[1]-1][i] == 'C' and A[p2[1]-1][i] == 'P':
                rank[2*j] = (p1[0]+1, p1[1])
            elif A[p1[1]-1][i] == 'P' and A[p2[1]-1][i] == 'G':
                rank[2*j] = (p1[0]+1, p1[1])
            elif A[p1[1]-1][i] == 'G' and A[p2[1]-1][i] == 'P':
                rank[2*j+1] = (p2[0]+1, p2[1])
            elif A[p1[1]-1][i] == 'C' and A[p2[1]-1][i] == 'G':
                rank[2*j+1] = (p2[0]+1, p2[1])
            elif A[p1[1]-1][i] == 'P' and A[p2[1]-1][i] == 'C':
                rank[2*j+1] = (p2[0]+1, p2[1])
        rank.sort(key=lambda x: (-x[0], x[1]))
    for r in rank:
        print(r[1])

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = [list(input()) for _ in range(2*n)]
    players = [i for i in range(2*n)]
    for i in range(m):
        players = sorted(players, key=lambda x: (a[x][i], x))
        for j in range(0, 2*n, 2):
            if a[players[j]][i] == 'G' and a[players[j+1]][i] == 'C':
                players[j+1], players[j] = players[j], players[j+1]
            elif a[players[j]][i] == 'C' and a[players[j+1]][i] == 'P':
                players[j+1], players[j] = players[j], players[j+1]
            elif a[players[j]][i] == 'P' and a[players[j+1]][i] == 'G':
                players[j+1], players[j] = players[j], players[j+1]
    for player in players:
        print(player+1)

=======
Suggestion 3

def rps(t1, t2):
    if t1 == 'G':
        if t2 == 'C':
            return 1
        elif t2 == 'P':
            return 2
        else:
            return 0
    elif t1 == 'C':
        if t2 == 'P':
            return 1
        elif t2 == 'G':
            return 2
        else:
            return 0
    else:
        if t2 == 'G':
            return 1
        elif t2 == 'C':
            return 2
        else:
            return 0

=======
Suggestion 4

def main():
    N, M = map(int, input().split())

    A = []
    for i in range(2 * N):
        A.append(input())

    B = []
    for i in range(2 * N):
        B.append([0, i + 1])

    for i in range(M):
        for j in range(N):
            a = B[2 * j][1] - 1
            b = B[2 * j + 1][1] - 1
            if A[a][i] == A[b][i]:
                continue

            if A[a][i] == 'G' and A[b][i] == 'C':
                B[2 * j][0] += 1
            elif A[a][i] == 'C' and A[b][i] == 'P':
                B[2 * j][0] += 1
            elif A[a][i] == 'P' and A[b][i] == 'G':
                B[2 * j][0] += 1
            else:
                B[2 * j + 1][0] += 1

        B.sort(key=lambda x: (-x[0], x[1]))

    for i in range(2 * N):
        print(B[i][1])

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = [input() for i in range(2*n)]
    b = [(i, 0) for i in range(2*n)]
    for i in range(m):
        c = []
        for j in range(n):
            a1, a2 = b[2*j]
            b1, b2 = b[2*j+1]
            if a[a1][i] == a[b1][i]:
                continue
            elif a[a1][i] == 'G':
                if a[b1][i] == 'C':
                    c.append((a1, 1))
                    c.append((b1, -1))
                elif a[b1][i] == 'P':
                    c.append((a1, -1))
                    c.append((b1, 1))
            elif a[a1][i] == 'C':
                if a[b1][i] == 'P':
                    c.append((a1, 1))
                    c.append((b1, -1))
                elif a[b1][i] == 'G':
                    c.append((a1, -1))
                    c.append((b1, 1))
            elif a[a1][i] == 'P':
                if a[b1][i] == 'G':
                    c.append((a1, 1))
                    c.append((b1, -1))
                elif a[b1][i] == 'C':
                    c.append((a1, -1))
                    c.append((b1, 1))
        c.sort(key=lambda x: x[0])
        c.sort(key=lambda x: x[1], reverse=True)
        b = c
    for i, j in b:
        print(i+1)

=======
Suggestion 6

def rock_scissors_paper():
    N, M = map(int, input().split())
    A = [input() for _ in range(2*N)]
    players = [[i+1, 0] for i in range(2*N)]
    for i in range(M):
        for j in range(N):
            p1 = players[2*j]
            p2 = players[2*j+1]
            h1 = A[p1[0]-1][i]
            h2 = A[p2[0]-1][i]
            if h1 == 'G' and h2 == 'C':
                p1[1] += 1
            elif h1 == 'C' and h2 == 'P':
                p1[1] += 1
            elif h1 == 'P' and h2 == 'G':
                p1[1] += 1
            elif h1 == h2:
                continue
            else:
                p2[1] += 1
        players.sort(key=lambda x: (-x[1], x[0]))
    for i in range(2*N):
        print(players[i][0])

rock_scissors_paper()

=======
Suggestion 7

def main():
    N,M = map(int,input().split())
    A = [input() for _ in range(2*N)]

    rank = [[i+1,0] for i in range(2*N)]
    for i in range(M):
        for j in range(N):
            a = A[rank[2*j][0]-1][i]
            b = A[rank[2*j+1][0]-1][i]

            if a == 'G' and b == 'C':
                rank[2*j][1] += 1
            elif a == 'C' and b == 'P':
                rank[2*j][1] += 1
            elif a == 'P' and b == 'G':
                rank[2*j][1] += 1
            elif a == 'G' and b == 'P':
                rank[2*j+1][1] += 1
            elif a == 'C' and b == 'G':
                rank[2*j+1][1] += 1
            elif a == 'P' and b == 'C':
                rank[2*j+1][1] += 1

        rank.sort(key=lambda x:(-x[1],x[0]))

    for i in range(2*N):
        print(rank[i][0])

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = [input() for _ in range(2 * N)]
    ranking = [(i, 0) for i in range(2 * N)]
    for i in range(M):
        for j in range(N):
            id1 = ranking[2 * j][0]
            id2 = ranking[2 * j + 1][0]
            hand1 = A[id1][i]
            hand2 = A[id2][i]
            if hand1 == hand2:
                continue
            if hand1 == "G" and hand2 == "C":
                ranking[2 * j][1] -= 1
            elif hand1 == "C" and hand2 == "P":
                ranking[2 * j][1] -= 1
            elif hand1 == "P" and hand2 == "G":
                ranking[2 * j][1] -= 1
            else:
                ranking[2 * j + 1][1] -= 1
        ranking.sort(key=lambda x: (x[1], x[0]))
    for i in range(2 * N):
        print(ranking[i][0] + 1)

=======
Suggestion 9

def rank_players(n, m, a):
    players = list(range(2*n))
    for i in range(m):
        new_players = []
        for j in range(n):
            p1 = players[2*j]
            p2 = players[2*j+1]
            if a[p1][i] == a[p2][i]:
                new_players.append(min(p1, p2))
            elif a[p1][i] == 'G' and a[p2][i] == 'C':
                new_players.append(p1)
            elif a[p1][i] == 'C' and a[p2][i] == 'P':
                new_players.append(p1)
            elif a[p1][i] == 'P' and a[p2][i] == 'G':
                new_players.append(p1)
            else:
                new_players.append(p2)
        players = new_players
    return players
