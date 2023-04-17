Synthesizing 10/10 solutions

=======

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W):
            if A[i][j] % 2 == 0:
                continue
            if j < W - 1:
                ans.append((i + 1, j + 1, i + 1, j + 2))
                A[i][j + 1] += 1
            elif i < H - 1:
                ans.append((i + 1, j + 1, i + 2, j + 1))
                A[i + 1][j] += 1
    print(len(ans))
    for a in ans:
        print(*a)

=======

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W):
            if A[i][j] % 2 == 1:
                if j < W - 1 and A[i][j + 1] % 2 == 1:
                    A[i][j] -= 1
                    A[i][j + 1] += 1
                    ans.append([i + 1, j + 1, i + 1, j + 2])
                elif i < H - 1 and A[i + 1][j] % 2 == 1:
                    A[i][j] -= 1
                    A[i + 1][j] += 1
                    ans.append([i + 1, j + 1, i + 2, j + 1])
    print(len(ans))
    for i in range(len(ans)):
        print(*ans[i])

=======

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W):
            if A[i][j] % 2 == 0:
                continue
            if j + 1 < W:
                ans.append((i, j, i, j + 1))
                A[i][j + 1] += 1
            elif i + 1 < H:
                ans.append((i, j, i + 1, j))
                A[i + 1][j] += 1
    print(len(ans))
    for a in ans:
        print(*[x + 1 for x in a])

=======

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W):
            if i == H - 1 and j == W - 1:
                break
            if j == W - 1:
                if A[i][j] % 2 == 1:
                    ans.append((i, j, i + 1, j + 1))
                    A[i + 1][j] += 1
            else:
                if A[i][j] % 2 == 1:
                    ans.append((i, j, i + 1, j + 1))
                    A[i + 1][j] += 1
    print(len(ans))
    for i, j, k, l in ans:
        print(i + 1, j + 1, k, l)

=======

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W):
            if A[i][j] % 2:
                if j < W - 1:
                    ans.append((i, j, i, j + 1))
                    A[i][j + 1] += 1
                elif i < H - 1:
                    ans.append((i, j, i + 1, j))
                    A[i + 1][j] += 1
    print(len(ans))
    for a in ans:
        print(*[i + 1 for i in a])

=======

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H)]
    ans = []
    for i in range(H):
        for j in range(W):
            if i + 1 < H and A[i][j] % 2 == 1:
                ans.append([i, j, i+1, j])
                A[i][j] -= 1
                A[i+1][j] += 1
            elif j + 1 < W and A[i][j] % 2 == 1:
                ans.append([i, j, i, j+1])
                A[i][j] -= 1
                A[i][j+1] += 1
    print(len(ans))
    for i in ans:
        print(*i)

=======

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    N = 0
    ans = []
    for i in range(H):
        for j in range(W):
            if A[i][j] % 2 == 1:
                N += 1
                if j != W - 1:
                    ans.append((i, j, i, j + 1))
                    A[i][j + 1] += 1
                elif i != H - 1:
                    ans.append((i, j, i + 1, j))
                    A[i + 1][j] += 1
    print(N)
    for i in range(N):
        print(ans[i][0] + 1, ans[i][1] + 1, ans[i][2] + 1, ans[i][3] + 1)

=======

def solve():
    H, W = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W-1):
            if a[i][j] % 2 == 1:
                ans.append([i+1, j+1, i+1, j+2])
                a[i][j] -= 1
                a[i][j+1] += 1
    for i in range(H-1):
        if a[i][W-1] % 2 == 1:
            ans.append([i+1, W, i+2, W])
            a[i][W-1] -= 1
            a[i+1][W-1] += 1
    print(len(ans))
    for i in ans:
        print(*i)

=======

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    N = 0
    for i in range(H):
        for j in range(W):
            if A[i][j] % 2 == 1:
                N += 1
    print(N)
    for i in range(H):
        for j in range(W):
            if A[i][j] % 2 == 1:
                if j < W - 1:
                    print(i + 1, j + 1, i + 1, j + 2)
                else:
                    print(i + 1, j + 1, i + 2, j + 1)

=======

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    # 0: right, 1: down
    direction = 0

    # 操作の回数は最大で H * W 回
    print(H * W)

    for i in range(H):
        for j in range(W):
            # 偶数の場合は移動しない
            if A[i][j] % 2 == 0:
                continue

            if direction == 0:
                # 奇数の場合は右に移動
                if j < W - 1:
                    print(i + 1, j + 1, i + 1, j + 2)
                # 右端の場合は下に移動
                else:
                    print(i + 1, j + 1, i + 2, j + 1)
            else:
                # 奇数の場合は下に移動
                if i < H - 1:
                    print(i + 1, j + 1, i + 2, j + 1)
                # 下端の場合は右に移動
                else:
                    print(i + 1, j + 1, i + 1, j + 2)

            # 方向を変える
            direction = 1 - direction
