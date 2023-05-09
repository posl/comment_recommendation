Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[False] * (Y + 1) for _ in range(X + 1)]
    dp[0][0] = True
    for i in range(N):
        for x in range(X, -1, -1):
            for y in range(Y, -1, -1):
                if dp[x][y]:
                    if x + A[i] <= X and y + B[i] <= Y:
                        dp[x + A[i]][y + B[i]] = True
    ans = -1
    for x in range(X + 1):
        for y in range(Y + 1):
            if dp[x][y]:
                if ans == -1:
                    ans = x + y
                else:
                    ans = min(ans, x + y)
    print(ans)

=======
Suggestion 2

def solve():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    dp = [[False] * (Y + 1) for i in range(X + 1)]
    dp[0][0] = True

    for i in range(N):
        for x in range(X, -1, -1):
            for y in range(Y, -1, -1):
                if dp[x][y] and x + A[i] <= X and y + B[i] <= Y:
                    dp[x + A[i]][y + B[i]] = True

    ans = -1
    for x in range(X + 1):
        for y in range(Y + 1):
            if dp[x][y]:
                ans = max(ans, x + y)

    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    X,Y = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a,b = map(int, input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    #print(X)
    #print(Y)
    #print(N)
    total = 0
    for i in range(N):
        total += A[i] + B[i]
    #print(total)
    if total < X + Y:
        print(-1)
    else:
        count = 0
        while X > 0 or Y > 0:
            if X > 0:
                max = 0
                max_index = 0
                for i in range(N):
                    if A[i] > max:
                        max = A[i]
                        max_index = i
                A[max_index] = -1
                count += 1
                X -= max
            if Y > 0:
                max = 0
                max_index = 0
                for i in range(N):
                    if B[i] > max:
                        max = B[i]
                        max_index = i
                B[max_index] = -1
                count += 1
                Y -= max
        print(count)
main()

=======
Suggestion 4

def main():
    n = int(input())
    x, y = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)

    dp = [[False for j in range(y+1)] for i in range(x+1)]
    dp[0][0] = True
    for i in range(n):
        for j in range(x, -1, -1):
            for k in range(y, -1, -1):
                if dp[j][k]:
                    dp[min(j+a[i], x)][min(k+b[i], y)] = True

    for i in range(min(x, y)+1):
        if dp[i][i]:
            print(i)
            break
    else:
        print(-1)

=======
Suggestion 5

def lunchbox():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[False]*(Y+1) for _ in range(X+1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(X, -1, -1):
            for k in range(Y, -1, -1):
                if dp[j][k]:
                    dp[min(X, j+A[i])][min(Y, k+B[i])] = True
    ans = -1
    for i in range(X+1):
        for j in range(Y+1):
            if dp[i][j]:
                ans = i+j
    return ans

print(lunchbox())

=======
Suggestion 6

def solve():
    N = int(input())
    X, Y = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(N)]

    dp = [[False] * (Y + 1) for _ in range(X + 1)]
    dp[0][0] = True
    for a, b in AB:
        for i in range(X, -1, -1):
            for j in range(Y, -1, -1):
                if dp[i][j] and i + a <= X and j + b <= Y:
                    dp[i + a][j + b] = True

    for i in range(1, X + 1):
        for j in range(1, Y + 1):
            if dp[i][j]:
                print(i + j)
                return
    print(-1)

=======
Suggestion 7

def main():
    n = int(input())
    x, y = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    dp = [[[False for _ in range(y+1)] for _ in range(x+1)] for _ in range(n+1)]
    dp[0][0][0] = True
    for i in range(n):
        a, b = ab[i]
        for j in range(x+1):
            for k in range(y+1):
                if dp[i][j][k]:
                    dp[i+1][j][k] = True
                    if j+a <= x and k+b <= y:
                        dp[i+1][j+a][k+b] = True
    for i in range(n, -1, -1):
        if dp[i][x][y]:
            print(i)
            return
    print(-1)

=======
Suggestion 8

def main():
    N = int(input())
    X, Y = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]

    dp = [[False] * (Y + 1) for _ in range(X + 1)]
    dp[0][0] = True

    for a, b in AB:
        for i in reversed(range(X + 1)):
            for j in reversed(range(Y + 1)):
                if dp[i][j]:
                    dp[min(X, i + a)][min(Y, j + b)] = True

    for i in range(1, N + 1):
        if dp[min(X, i * AB[i - 1][0])][min(Y, i * AB[i - 1][1])]:
            print(i)
            break
    else:
        print(-1)

=======
Suggestion 9

def main():
    N = int(input())
    X, Y = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0] + x[1], reverse=True)
    dp = [[False for _ in range(Y + 1)] for _ in range(X + 1)]
    dp[0][0] = True
    for a, b in AB:
        for x in range(X, -1, -1):
            for y in range(Y, -1, -1):
                if dp[x][y] and x + a <= X and y + b <= Y:
                    dp[x + a][y + b] = True
    for x in range(X, -1, -1):
        for y in range(Y, -1, -1):
            if dp[x][y]:
                print(X + Y - x - y)
                exit()
    print(-1)

=======
Suggestion 10

def main():
    n = int(input())
    x, y = map(int, input().split())
    lunchboxes = [tuple(map(int, input().split())) for _ in range(n)]
    dp = [[False] * (y+1) for _ in range(x+1)]
    dp[0][0] = True
    for a, b in lunchboxes:
        for i in range(x, -1, -1):
            for j in range(y, -1, -1):
                if dp[i][j] and i+a <= x and j+b <= y:
                    dp[i+a][j+b] = True
    for i in range(x+1):
        for j in range(y+1):
            if dp[x-i][y-j]:
                print(x-i+y-j)
                return
    print(-1)
