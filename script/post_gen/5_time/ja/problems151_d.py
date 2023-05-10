Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == ".":
                ans += 1
    print(ans - 1)

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == ".":
                ans += 1
    if ans == H*W:
        print(ans-1)
    else:
        print(ans)

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == ".":
                # 右方向
                cnt = 0
                k = j
                while k < W:
                    if S[i][k] == "#":
                        break
                    else:
                        cnt += 1
                    k += 1
                # 左方向
                k = j
                while k >= 0:
                    if S[i][k] == "#":
                        break
                    else:
                        cnt += 1
                    k -= 1
                # 上方向
                k = i
                while k >= 0:
                    if S[k][j] == "#":
                        break
                    else:
                        cnt += 1
                    k -= 1
                # 下方向
                k = i
                while k < H:
                    if S[k][j] == "#":
                        break
                    else:
                        cnt += 1
                    k += 1
                ans = max(ans, cnt-3)
    print(ans)
main()

=======
Suggestion 4

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]

    # 4方向
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                continue

            # BFS
            dist = [[-1] * w for _ in range(h)]
            dist[i][j] = 0
            q = [(i, j)]

            while q:
                y, x = q.pop(0)

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if nx < 0 or w <= nx or ny < 0 or h <= ny:
                        continue

                    if s[ny][nx] == '#':
                        continue

                    if dist[ny][nx] != -1:
                        continue

                    dist[ny][nx] = dist[y][x] + 1
                    q.append((ny, nx))

            for k in range(h):
                for l in range(w):
                    if dist[k][l] == -1:
                        continue

                    ans = max(ans, dist[k][l])

    print(ans)

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]

    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                continue
            d = [[-1] * w for _ in range(h)]
            d[i][j] = 0
            q = [(i, j)]
            while q:
                y, x = q.pop(0)
                for dy, dx in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    ny, nx = y + dy, x + dx
                    if ny < 0 or nx < 0 or ny >= h or nx >= w:
                        continue
                    if s[ny][nx] == '#':
                        continue
                    if d[ny][nx] == -1:
                        d[ny][nx] = d[y][x] + 1
                        q.append((ny, nx))
            ans = max(ans, max([max(l) for l in d]))
    print(ans)

main()

=======
Suggestion 6

def get_input():
    H, W = map(int, input().split())
    S = []
    for _ in range(H):
        S.append(input())
    return H, W, S

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]

    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                # 上下左右に道があるか確認
                if i > 0 and S[i-1][j] == '.':
                    ans += 1
                if i < H-1 and S[i+1][j] == '.':
                    ans += 1
                if j > 0 and S[i][j-1] == '.':
                    ans += 1
                if j < W-1 and S[i][j+1] == '.':
                    ans += 1

    print(ans)

=======
Suggestion 8

def main():
    h,w = map(int,input().split())
    s = [list(input()) for i in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '.':
                ans += 1
    print(ans-1)

=======
Suggestion 9

def solve():
    # H, W = map(int, input().split())
    # S = [input() for _ in range(H)]
    H, W = 3, 3
    S = ['...', '...', '...']
    print(H, W)
    print(S)

    res = 0
    print(res)

=======
Suggestion 10

def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]

    ans = 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == '.':
                ans += 1

    if ans == H * W:
        print(ans - 1)
    else:
        print(ans)

main()
