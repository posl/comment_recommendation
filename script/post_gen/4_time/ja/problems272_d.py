Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N,M = map(int,input().split())
    ans = [[-1 for _ in range(N)] for _ in range(N)]
    ans[0][0] = 0
    for i in range(N):
        for j in range(N):
            if ans[i][j] == -1:
                continue
            for k in range(N):
                for l in range(N):
                    if ans[k][l] == -1 and (i-k)**2 + (j-l)**2 <= M:
                        ans[k][l] = ans[i][j] + 1
    for i in range(N):
        print(*ans[i])

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    if m == 1:
        for i in range(n):
            for j in range(n):
                print(i+j)
            print()
    else:
        for i in range(n):
            for j in range(n):
                if i == 0 and j == 0:
                    print(0, end="")
                else:
                    print(-1, end="")
                if j < n-1:
                    print(" ", end="")
            print()

=======
Suggestion 3

def main():
    N,M = map(int,input().split())
    if N == 1:
        print(0)
        return
    if M == 1:
        for i in range(N):
            print(i)
        return
    if N == 2:
        if M == 2:
            print(1,2)
            print(2,1)
        elif M == 3:
            print(0,1)
            print(1,2)
        elif M == 4:
            print(1,1)
            print(1,2)
        elif M == 5:
            print(0,1)
            print(1,2)
        elif M == 6:
            print(1,2)
            print(2,2)
        elif M == 7:
            print(0,1)
            print(1,2)
        elif M == 8:
            print(1,1)
            print(1,2)
        elif M == 9:
            print(0,1)
            print(1,2)
    elif N == 3:
        if M == 2:
            print(1,2,3)
            print(2,1,2)
            print(3,2,3)
        elif M == 3:
            print(0,1,2)
            print(1,2,3)
            print(2,3,4)
        elif M == 4:
            print(1,1,2)
            print(1,2,3)
            print(2,3,4)
        elif M == 5:
            print(0,1,2)
            print(1,2,3)
            print(2,3,4)
        elif M == 6:
            print(1,2,3)
            print(2,3,3)
            print(3,3,4)
        elif M == 7:
            print(0,1,2)
            print(1,2,3)
            print(2,3,4)
        elif M == 8:
            print(1,1,2)
            print(1,2,3)
            print(2,3,4)
        elif M == 9:
            print(0,1,2)
            print(1,2,3)
            print(2,3,

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    if M == 1:
        print('\n'.join(' '.join(map(str, range(i, i + N))) for i in range(1, N * N + 1, N)))
        return
    ans = [[-1] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                ans[i][j] = 0
            elif i == 0:
                ans[i][j] = ans[i][j - 1] + 1
            elif j == 0:
                ans[i][j] = ans[i - 1][j] + 1
            else:
                ans[i][j] = min(ans[i - 1][j], ans[i][j - 1]) + 1
    print('\n'.join(' '.join(map(str, ans[i])) for i in range(N)))

=======
Suggestion 5

def solve():
    N, M = map(int, input().split())
    N2 = N ** 2
    M2 = M ** 2
    ans = [[-1] * N for _ in range(N)]
    ans[0][0] = 0
    for i in range(N):
        for j in range(N):
            if ans[i][j] == -1:
                continue
            for k in range(N):
                for l in range(N):
                    if ans[k][l] != -1:
                        continue
                    if (i - k) ** 2 + (j - l) ** 2 == M2:
                        ans[k][l] = ans[i][j] + 1
    for i in range(N):
        print(*ans[i])

solve()

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    if M == 1:
        for i in range(N):
            for j in range(N):
                print(i+j)
            print()
        return

    # 1 から M までの平方数を求める
    # 1 は除く
    squares = []
    for i in range(2, M + 1):
        if i * i > M:
            break
        squares.append(i * i)

    # 各マスの最小手数を求める
    # 各マスは 1 から 2 * N - 1 までの手数で到達可能
    # ただし、マス (1, 1) は 0 手で到達可能
    # 到達不可能な場合は -1
    # マス (i, j) からマス (k, l) への距離は ((i-k)^2+(j-l)^2)^(1/2)
    # これは (i-k)^2+(j-l)^2 と等しい
    # ここで (i-k)^2+(j-l)^2 はマンハッタン距離の 2 乗
    # つまり、マンハッタン距離を 2 乗したものが平方数であれば到達可能
    # 平方数の最小のものが最小手数
    # ただし、マンハッタン距離が 0 の場合は 0 手で到達可能とする
    # また、マンハッタン距離が 0 でないのに平方数でない場合は -1 とする
    # ただし、マンハッタン距離が 0 でないのに平方数でない場合は -1 とする
    # これは、平方数でない場合は平方数である場所を経由して

=======
Suggestion 7

def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    N, M = map(int, input().split())
    if M == 1:
        print("\n".join(" ".join(str(i + j) for j in range(N)) for i in range(N)))
        return
    sq = int(M ** 0.5)
    if sq * sq == M:
        sq -= 1
    sq += 1
    sq2 = sq * sq
    dist = [[-1] * N for _ in range(N)]
    dist[0][0] = 0
    que = deque([(0, 0)])
    while que:
        x, y = que.popleft()
        for dx, dy in ((-sq, 0), (sq, 0), (0, -sq), (0, sq)):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                que.append((nx, ny))
    print("\n".join(" ".join(str(dist[i][j]) for j in range(N)) for i in range(N)))

=======
Suggestion 8

def calc(x,y):
    return int(((x-y)**2)**0.5)

n,m = map(int,input().split())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == 1 and j == 1:
            print(0,end=" ")
        else:
            print(calc(1,i)+calc(1,j),end=" ")
    print()

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    #print(n,m)
    #n = 3
    #m = 1
    #n = 10
    #m = 5
    #n = 400
    #m = 1000000
    #n = 1
    #m = 1
    #n = 2
    #m = 1
    #n = 2
    #m = 2
    #n = 2
    #m = 3
    #n = 2
    #m = 4
    #n = 2
    #m = 5
    #n = 2
    #m = 6
    #n = 2
    #m = 7
    #n = 2
    #m = 8
    #n = 2
    #m = 9
    #n = 2
    #m = 10
    #n = 2
    #m = 11
    #n = 2
    #m = 12
    #n = 2
    #m = 13
    #n = 2
    #m = 14
    #n = 2
    #m = 15
    #n = 2
    #m = 16
    #n = 2
    #m = 17
    #n = 2
    #m = 18
    #n = 2
    #m = 19
    #n = 2
    #m = 20
    #n = 2
    #m = 21
    #n = 2
    #m = 22
    #n = 2
    #m = 23
    #n = 2
    #m = 24
    #n = 2
    #m = 25
    #n = 2
    #m = 26
    #n = 2
    #m = 27
    #n = 2
    #m = 28
    #n = 2
    #m = 29
    #n = 2
    #m = 30
    #n =

=======
Suggestion 10

def main():
    N,M = map(int,input().split())
    print(N,M)
    print("Hello World!")
    return
