Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j]
    ans -= H * W * min([min(A[i]) for i in range(H)])
    print(ans)

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j]
    print(ans - H * W * min(min(A)))

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j]
    print(ans - H * W)

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = 100 * 100
    for h in range(H):
        for w in range(W):
            cnt = 0
            for i in range(H):
                for j in range(W):
                    cnt += abs(i - h) + abs(j - w)
            ans = min(ans, cnt * A[h][w])
    print(ans)

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H)]
    B = [[0] * W for i in range(H)]
    for i in range(H):
        for j in range(W):
            B[i][j] = A[i][j] % 2
    ans = 0
    for i in range(H):
        for j in range(W):
            if B[i][j] == 1:
                if i < H-1:
                    B[i+1][j] += 1
                    ans += 1
                elif j < W-1:
                    B[i][j+1] += 1
                    ans += 1
    print(ans)
main()

=======
Suggestion 6

def main():
    H,W = map(int,input().split())
    A = [list(map(int,input().split())) for _ in range(H)]
    ans = 10**10
    for i in range(H):
        for j in range(W):
            tmp = 0
            for k in range(H):
                for l in range(W):
                    tmp += abs(i-k) + abs(j-l) + abs(A[i][j]-A[k][l])
            ans = min(ans,tmp)
    print(ans)

=======
Suggestion 7

def main():
    #input
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    #compute
    s = 0
    for i in range(H):
        for j in range(W):
            s += A[i][j]
    if s % (H*W) != 0:
        print(-1)
        return
    s //= (H*W)
    for i in range(H):
        for j in range(W):
            if A[i][j] > s:
                A[i][j] -= s
            else:
                A[i][j] = 0
    ans = 0
    for i in range(H):
        for j in range(W):
            if A[i][j] > 0:
                ans += 1
                A[i][j] = 0
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                        nx = x + dx
                        ny = y + dy
                        if 0 <= nx < H and 0 <= ny < W and A[nx][ny] > 0:
                            A[nx][ny] = 0
                            stack.append((nx, ny))
    print(ans)

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    ans = 10000
    for h in range(H):
        for w in range(W):
            tmp = 0
            for i in range(H):
                for j in range(W):
                    tmp += abs(A[h][w] - A[i][j])
            ans = min(ans, tmp)
    print(ans)

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    A = [item for sublist in A for item in sublist]
    A = [x for x in A if x != 0]
    print(sum(A) - len(A) * min(A))

=======
Suggestion 10

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    sumA = sum(sum(a) for a in A)
    if sumA % (H*W) != 0:
        print(-1)
        return

    ave = sumA // (H*W)
    ans = 0
    for i in range(H):
        for j in range(W):
            if (i+j) % 2 == 0:
                if A[i][j] > ave:
                    ans += A[i][j] - ave
            else:
                if A[i][j] < ave:
                    ans += ave - A[i][j]

    print(ans)
