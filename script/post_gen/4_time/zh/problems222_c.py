Synthesizing 10/10 solutions

=======
Suggestion 1

def f(x):
    return x[1]

=======
Suggestion 2

def win(a, b):
    if a == 'G' and b == 'C':
        return True
    elif a == 'C' and b == 'P':
        return True
    elif a == 'P' and b == 'G':
        return True
    else:
        return False

n, m = map(int, input().split())
a = [input() for _ in range(2 * n)]
rank = [[i + 1, 0] for i in range(2 * n)]
for i in range(m):
    for j in range(n):
        p1, p2 = rank[2 * j][0] - 1, rank[2 * j + 1][0] - 1
        if win(a[p1][i], a[p2][i]):
            rank[2 * j][1] -= 1
        elif win(a[p2][i], a[p1][i]):
            rank[2 * j + 1][1] -= 1
    rank.sort(key=lambda x: (x[1], x[0]))
for i in range(2 * n):
    print(rank[i][0])

=======
Suggestion 3

def get_winner(player1, player2):
    if player1 == player2:
        return player1
    elif player1 == 'G':
        if player2 == 'C':
            return player1
        else:
            return player2
    elif player1 == 'C':
        if player2 == 'P':
            return player1
        else:
            return player2
    elif player1 == 'P':
        if player2 == 'G':
            return player1
        else:
            return player2

=======
Suggestion 4

def rps(a, b):
    if a == b:
        return 0
    elif (a == "G" and b == "C") or (a == "C" and b == "P") or (a == "P" and b == "G"):
        return 1
    else:
        return -1

n, m = map(int, input().split())
a = [list(input()) for _ in range(2*n)]
rank = [[i, 0] for i in range(2*n)]

for i in range(m):
    for j in range(n):
        idx1, idx2 = rank[2*j][0], rank[2*j+1][0]
        res = rps(a[idx1][i], a[idx2][i])
        if res == 1:
            rank[2*j][1] -= 1
        elif res == -1:
            rank[2*j+1][1] -= 1
    rank.sort(key=lambda x: (x[1], x[0]))

for i in range(2*n):
    print(rank[i][0]+1)

=======
Suggestion 5

def game(a,b):
    if a == b:
        return 0
    elif a == 'G' and b == 'C':
        return 1
    elif a == 'C' and b == 'P':
        return 1
    elif a == 'P' and b == 'G':
        return 1
    else:
        return 2

=======
Suggestion 6

def jiaquan(a):
    if a == 'G':
        return 0
    elif a == 'C':
        return 1
    else:
        return 2

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    a = [input() for _ in range(2*n)]
    rank = [[i,0] for i in range(2*n)]
    for i in range(m):
        for j in range(n):
            p1,p2 = rank[2*j][0],rank[2*j+1][0]
            if a[p1][i] == a[p2][i]:
                continue
            elif a[p1][i] == "G" and a[p2][i] == "C":
                rank[2*j][1] -= 1
            elif a[p1][i] == "C" and a[p2][i] == "P":
                rank[2*j][1] -= 1
            elif a[p1][i] == "P" and a[p2][i] == "G":
                rank[2*j][1] -= 1
            else:
                rank[2*j][1] += 1
    rank.sort(key=lambda x: (x[1],x[0]))
    for i in range(2*n):
        print(rank[i][0]+1)

=======
Suggestion 8

def main():
    n,m=map(int,input().split())
    a=[]
    for i in range(2*n):
        a.append(input())
    ans=[]
    for i in range(2*n):
        ans.append([0,i+1])
    for i in range(m):
        for j in range(n):
            p1=ans[2*j][1]-1
            p2=ans[2*j+1][1]-1
            if a[p1][i]==a[p2][i]:
                continue
            elif a[p1][i]=='G' and a[p2][i]=='C':
                ans[2*j][0]-=1
            elif a[p1][i]=='C' and a[p2][i]=='P':
                ans[2*j][0]-=1
            elif a[p1][i]=='P' and a[p2][i]=='G':
                ans[2*j][0]-=1
            else:
                ans[2*j+1][0]-=1
        ans.sort(reverse=True)
    for i in range(2*n):
        print(ans[i][1])

main()

=======
Suggestion 9

def main():
    n,m=map(int,input().split())
    a=[]
    for i in range(2*n):
        a.append(input())
    rank=[[i+1,0] for i in range(2*n)]
    for i in range(m):
        for j in range(n):
            if a[rank[2*j][0]-1][i]==a[rank[2*j+1][0]-1][i]:
                continue
            elif a[rank[2*j][0]-1][i]=="G" and a[rank[2*j+1][0]-1][i]=="C":
                rank[2*j][1]+=1
            elif a[rank[2*j][0]-1][i]=="C" and a[rank[2*j+1][0]-1][i]=="P":
                rank[2*j][1]+=1
            elif a[rank[2*j][0]-1][i]=="P" and a[rank[2*j+1][0]-1][i]=="G":
                rank[2*j][1]+=1
            else:
                rank[2*j+1][1]+=1
        rank.sort(key=lambda x:(-x[1],x[0]))
    for i in range(2*n):
        print(rank[i][0])

main()

=======
Suggestion 10

def compare(x,y):
    if x[0] > y[0]:
        return -1
    elif x[0] < y[0]:
        return 1
    else:
        if x[1] < y[1]:
            return -1
        elif x[1] > y[1]:
            return 1
        else:
            return 0
