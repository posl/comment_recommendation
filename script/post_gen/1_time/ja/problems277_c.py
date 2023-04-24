Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    A.sort()
    B.sort()
    if N % 2 == 0:
        print(B[N//2] - A[N//2 - 1] + 1)
    else:
        print(B[N//2] - A[N//2] + 1)

=======
Suggestion 2

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    A.sort()
    B.sort()

    if N % 2 == 0:
        print(B[N // 2] - A[N // 2] + 1)
    else:
        print(B[N // 2] - A[N // 2] + 1)

=======
Suggestion 3

def main():
    N = int(input())
    H = []
    for _ in range(N):
        A, B = map(int, input().split())
        H.append(A)
        H.append(B)
    H = list(set(H))
    H.sort()
    H = {h:i for i, h in enumerate(H)}
    G = [[] for _ in range(len(H))]
    for _ in range(N):
        A, B = map(int, input().split())
        G[H[A]].append(H[B])
        G[H[B]].append(H[A])
    INF = 10**18
    dist = [INF] * len(H)
    dist[0] = 0
    que = [0]
    while que:
        v = que.pop()
        for nv in G[v]:
            if dist[nv] == INF:
                dist[nv] = dist[v] + 1
                que.append(nv)
    print(max(dist))

=======
Suggestion 4

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    ans = 0
    for a, b in AB:
        ans = max(ans, b)
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    ans = AB[0][1]
    for i in range(1, N):
        ans = max(ans, AB[i][1])
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[1])
    ans = 1
    for a, b in AB:
        if a > ans:
            ans = a
        else:
            ans = b
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    ans = 0
    for a, b in AB:
        if a <= ans:
            ans = max(ans, b)
        else:
            ans = a
    print(ans)

=======
Suggestion 8

def main():
    #input
    N = int(input())
    AB = [[int(i) for i in input().split()] for _ in range(N)]

    #compute
    AB.sort(key=lambda x: x[0])
    ans = 1
    for i in range(N):
        ans = max(ans, AB[i][1])
        if i < N-1:
            ans = max(ans, AB[i+1][0])

    #output
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    #print(AB)
    max_floor = 0
    for i in range(N):
        if max_floor < AB[i][0]:
            max_floor = AB[i][0]
        if max_floor < AB[i][1]:
            max_floor = AB[i][1]
    print(max_floor)

=======
Suggestion 10

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]

    # はしごの始点・終点をそれぞれリスト化
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i] = AB[i][0]
        B[i] = AB[i][1]

    # はしごの始点・終点をそれぞれソート
    A.sort()
    B.sort()

    # はしごの始点の最大値と終点の最小値の差を出力
    print(B[-1] - A[0])
