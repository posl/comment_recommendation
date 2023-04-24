Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    P.sort(key=lambda x: x[0] + x[1] + x[2], reverse=True)
    print('Yes' if P[K-1][0] + P[K-1][1] + P[K-1][2] >= P[K][0] + P[K][1] + P[K][2] else 'No')
    for i in range(K, N):
        print('Yes' if P[K-1][0] + P[K-1][1] + P[K-1][2] == P[i][0] + P[i][1] + P[i][2] else 'No')

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    P.sort(key=lambda x: x[0] + x[1] + x[2], reverse=True)
    print("Yes" if P[K-1][0] + P[K-1][1] + P[K-1][2] >= P[K][0] + P[K][1] + P[K][2] else "No")

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    P = []
    for i in range(N):
        P.append(list(map(int, input().split())))
    P.sort(key=lambda x: x[0] + x[1] + x[2])
    P = P[::-1]
    s = sum(P[K - 1])
    for i in range(N):
        if sum(P[i]) >= s:
            print('Yes')
        else:
            print('No')

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    for p in P:
        p.append(sum(p))
    P.sort(key=lambda x: x[3], reverse=True)
    print(*['Yes' if p[3] >= P[K-1][3] else 'No' for p in P], sep='

')

=======
Suggestion 5

def get_input():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    return N, K, P

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    P.sort(key=lambda x: sum(x), reverse=True)
    print("Yes" if sum(P[K-1]) > sum(P[K]) else "No")

=======
Suggestion 7

def main():
    #input
    N, K = map(int, input().split())
    P = [[0]*4 for _ in range(N)]
    for i in range(N):
        P[i][0], P[i][1], P[i][2] = map(int, input().split())
    #compute
    for i in range(N):
        P[i][3] = 300 - P[i][2]
    P.sort(key=lambda x: x[0]+x[1]+x[2]+x[3], reverse=True)
    #output
    for i in range(N):
        if P[i][0]+P[i][1]+P[i][2]+P[i][3] >= P[K-1][0]+P[K-1][1]+P[K-1][2]+P[K-1][3]:
            print('Yes')
        else:
            print('No')

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        P[i].sort()
        P[i].reverse()
    P.sort()
    P.reverse()
    for i in range(N):
        if P[i][0] + P[i][1] + P[i][2] + P[i][3] >= P[K-1][0] + P[K-1][1] + P[K-1][2] + P[K-1][3]:
            print('Yes')
        else:
            print('No')

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        P[i].sort()
        P[i].reverse()
        P[i] = P[i][0] + P[i][1] + P[i][2]
    P.sort()
    P.reverse()
    if P[K-1] >= sum(P[:K]):
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    N,K = map(int,input().split())
    P = [list(map(int,input().split())) for _ in range(N)]

    total = [0]*N
    for i in range(N):
        total[i] = sum(P[i])
    
    rank = [0]*N
    for i in range(N):
        rank[i] = sum([total[j]>total[i] for j in range(N)])+1

    for i in range(N):
        if rank[i]<=K:
            print('Yes')
        else:
            print('No')
