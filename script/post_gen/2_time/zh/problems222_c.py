Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = [list(input()) for _ in range(2*n)]
    rank = [[i, 0] for i in range(2*n)]
    for i in range(m):
        for j in range(n):
            p1 = rank[2*j][0]
            p2 = rank[2*j+1][0]
            if a[p1][i] == a[p2][i]:
                continue
            elif a[p1][i] == 'G' and a[p2][i] == 'C':
                rank[2*j][1] -= 1
            elif a[p1][i] == 'C' and a[p2][i] == 'P':
                rank[2*j][1] -= 1
            elif a[p1][i] == 'P' and a[p2][i] == 'G':
                rank[2*j][1] -= 1
            else:
                rank[2*j][1] += 1
    rank.sort(key=lambda x: (x[1], x[0]), reverse=True)
    for i in range(2*n):
        print(rank[i][0]+1)
main()

=======
Suggestion 2

def rsp(a,b):
    if a == b:
        return a
    elif a == "G" and b == "C":
        return a
    elif a == "C" and b == "P":
        return a
    elif a == "P" and b == "G":
        return a
    else:
        return b

=======
Suggestion 3

def f(a,b):
    if a == "G" and b == "C":
        return 1
    elif a == "C" and b == "P":
        return 1
    elif a == "P" and b == "G":
        return 1
    elif a == b:
        return 0
    else:
        return -1

n,m = map(int,input().split())
a = []
for i in range(2*n):
    a.append(input())
rank = [[i+1,0] for i in range(2*n)]
for i in range(m):
    for j in range(n):
        if f(a[rank[2*j][0]-1][i],a[rank[2*j+1][0]-1][i]) == 1:
            rank[2*j][1] += 1
        elif f(a[rank[2*j][0]-1][i],a[rank[2*j+1][0]-1][i]) == -1:
            rank[2*j+1][1] += 1
rank.sort(key=lambda x:x[1],reverse=True)
for i in range(2*n):
    print(rank[i][0])

=======
Suggestion 4

def judge(a, b):
    if a == b:
        return 0
    elif a == "G" and b == "C":
        return 1
    elif a == "G" and b == "P":
        return -1
    elif a == "C" and b == "P":
        return 1
    elif a == "C" and b == "G":
        return -1
    elif a == "P" and b == "G":
        return 1
    elif a == "P" and b == "C":
        return -1

n, m = map(int, input().split())
a = []
for i in range(2*n):
    a.append(input())

rank = [[0]*2 for i in range(n*2)]
for i in range(n*2):
    rank[i][0] = 0
    rank[i][1] = i + 1

for i in range(m):
    for j in range(n):
        p1 = rank[2*j][1] - 1
        p2 = rank[2*j+1][1] - 1
        result = judge(a[p1][i], a[p2][i])
        if result == 1:
            rank[2*j][0] -= 1
        elif result == -1:
            rank[2*j+1][0] -= 1
    rank.sort()

for i in range(n*2):
    print(rank[i][1])

=======
Suggestion 5

def solve():
    n,m=map(int,input().split())
    a=[input() for _ in range(2*n)]
    r=[[i+1,0] for i in range(2*n)]
    for i in range(m):
        for j in range(0,2*n,2):
            if a[r[j][0]-1][i]==a[r[j+1][0]-1][i]:
                continue
            elif a[r[j][0]-1][i]=='G' and a[r[j+1][0]-1][i]=='C':
                r[j][1]-=1
            elif a[r[j][0]-1][i]=='C' and a[r[j+1][0]-1][i]=='P':
                r[j][1]-=1
            elif a[r[j][0]-1][i]=='P' and a[r[j+1][0]-1][i]=='G':
                r[j][1]-=1
            else:
                r[j+1][1]-=1
        r.sort(key=lambda x:(x[1],-x[0]))
    for i in range(2*n):
        print(r[i][0])

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def check_win(p1,p2):
    if p1 == p2:
        return 0
    elif p1 == 'G' and p2 == 'C':
        return 1
    elif p1 == 'C' and p2 == 'P':
        return 1
    elif p1 == 'P' and p2 == 'G':
        return 1
    else:
        return -1

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    a = [input() for _ in range(2*n)]
    rank = [[i+1, 0] for i in range(2*n)]
    for i in range(m):
        for j in range(n):
            p1 = rank[2*j][0]-1
            p2 = rank[2*j+1][0]-1
            if a[p1][i] == 'G':
                if a[p2][i] == 'C':
                    rank[2*j][1] += 1
                elif a[p2][i] == 'P':
                    rank[2*j+1][1] += 1
            elif a[p1][i] == 'C':
                if a[p2][i] == 'P':
                    rank[2*j][1] += 1
                elif a[p2][i] == 'G':
                    rank[2*j+1][1] += 1
            elif a[p1][i] == 'P':
                if a[p2][i] == 'G':
                    rank[2*j][1] += 1
                elif a[p2][i] == 'C':
                    rank[2*j+1][1] += 1
        rank.sort(key=lambda x: (-x[1], x[0]))
    for i in range(2*n):
        print(rank[i][0])

=======
Suggestion 9

def f(x,y):
    if x==y:
        return 0
    if x=='G':
        if y=='C':
            return 1
        else:
            return -1
    if x=='C':
        if y=='P':
            return 1
        else:
            return -1
    if x=='P':
        if y=='G':
            return 1
        else:
            return -1
    return 0

=======
Suggestion 10

def main():
    n,m = map(int,input().split())
    A = []
    for i in range(2*n):
        A.append(input())
    rank = [i for i in range(2*n)]
    for i in range(m):
        rank = sorted(rank,key=lambda x:(A[x][i],x))
    for i in rank[::-1]:
        print(i+1)
