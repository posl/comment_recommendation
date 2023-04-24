Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    P.sort(key=lambda x: x[0] + x[1] + x[2])
    for i in range(N):
        if P[i][0] + P[i][1] + P[i][2] >= P[K - 1][0] + P[K - 1][1] + P[K - 1][2]:
            print('Yes')
        else:
            print('No')

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    P = []
    for _ in range(N):
        P.append(list(map(int, input().split())))
    P.sort(key=lambda x: x[0] + x[1] + x[2] + x[3], reverse=True)
    print("Yes" if P[K-1][0] + P[K-1][1] + P[K-1][2] + P[K-1][3] >= P[K][0] + P[K][1] + P[K][2] + P[K][3] else "No")

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    P = [[sum(p), p[0], p[1], p[2]] for p in P]
    P.sort(reverse=True)
    for i in range(N):
        if P[i][0] + P[i][1] + P[i][2] + P[i][3] < P[K - 1][0]:
            print('No')
        else:
            print('Yes')

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    for p in P:
        p.sort()
    P.sort(key=lambda x: x[0])
    for i in range(N):
        if i < K - 1 or P[i][0] + P[i][1] + P[i][2] + P[i][3] >= P[K - 1][0] + P[K - 1][1] + P[K - 1][2] + P[K - 1][3]:
            print("Yes")
        else:
            print("No")

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        P[i].sort()
    P.sort()
    for i in range(N):
        if sum(P[i]) >= sum(P[K-1]):
            print("Yes")
        else:
            print("No")

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    P = [[int(i) for i in input().split()] for j in range(N)]
    for i in range(N):
        if sum(P[i]) + 100 * (3 - P[i].count(300)) >= 400 * K:
            print('Yes')
        else:
            print('No')

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for i in range(N)]
    for i in range(N):
        if sum(P[i]) >= 100 * (4 - K):
            print("Yes")
        else:
            print("No")

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    C = [sum(p) for p in P]
    C.sort(reverse=True)
    print('Yes' if C[K-1] == C[K] else 'No')

=======
Suggestion 9

def main():
    N,K = map(int,input().split())
    P = [list(map(int,input().split())) for _ in range(N)]
    P.sort(key=lambda x:sum(x),reverse=True)
    print('Yes' if sum(P[K-1])<sum(P[K]) else 'No')

=======
Suggestion 10

def main():
    N,K=map(int,input().split())
    P=[list(map(int,input().split())) for _ in range(N)]
    S=[sum(p) for p in P]
    T=[sum(p[:3]) for p in P]
    T.sort()
    for i in range(N):
        if S[i]+T[N-K]<T[N-K-1]+300:
            print("No")
        else:
            print("Yes")

main()
