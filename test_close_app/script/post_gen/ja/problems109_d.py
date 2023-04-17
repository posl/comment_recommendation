Synthesizing 10/10 solutions

=======

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W):
            if A[i][j] % 2 == 1:
                if (i, j) == (H - 1, W - 1):
                    continue
                elif j == W - 1:
                    ans.append([i + 1, j + 1, i + 2, j + 1])
                    A[i][j] -= 1
                    A[i + 1][j] += 1
                else:
                    ans.append([i + 1, j + 1, i + 1, j + 2])
                    A[i][j] -= 1
                    A[i][j + 1] += 1
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1], ans[i][2], ans[i][3])

=======

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W):
            if A[i][j] % 2 == 1:
                if j < W - 1:
                    A[i][j] -= 1
                    A[i][j + 1] += 1
                    ans.append([i + 1, j + 1, i + 1, j + 2])
                else:
                    A[i][j] -= 1
                    A[i + 1][j] += 1
                    ans.append([i + 1, j + 1, i + 2, j + 1])
    print(len(ans))
    for a in ans:
        print(*a)

=======

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for h in range(H):
        for w in range(W):
            if (h + w) % 2 == 0 and A[h][w] % 2 == 1:
                if w < W - 1:
                    ans.append((h + 1, w + 1, h + 1, w + 2))
                    A[h][w + 1] += 1
                elif h < H - 1:
                    ans.append((h + 1, w + 1, h + 2, w + 1))
                    A[h + 1][w] += 1
    print(len(ans))
    for h, w, h2, w2 in ans:
        print(h, w, h2, w2)

=======

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    ans = []
    for h in range(H):
        for w in range(W):
            if A[h][w] % 2 == 1:
                if h == H-1 and w == W-1:
                    break
                if w == W-1:
                    A[h+1][w] += 1
                    ans.append([h+1, w+1, h+2, w+1])
                else:
                    A[h][w+1] += 1
                    ans.append([h+1, w+1, h+1, w+2])

    print(len(ans))
    for a in ans:
        print(*a)

=======

def main():
    H, W = map(int, input().split())
    A = []
    for _ in range(H):
        A.append(list(map(int, input().split())))
    ans = []
    for i in range(H):
        for j in range(W):
            if A[i][j] % 2 == 1:
                if j < W - 1:
                    A[i][j] -= 1
                    A[i][j + 1] += 1
                    ans.append([i + 1, j + 1, i + 1, j + 2])
                elif i < H - 1:
                    A[i][j] -= 1
                    A[i + 1][j] += 1
                    ans.append([i + 1, j + 1, i + 2, j + 1])
    print(len(ans))
    for a in ans:
        print(' '.join(map(str, a)))

=======

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    ans = []
    for i in range(H):
        for j in range(W-1):
            if A[i][j] % 2 == 1:
                ans.append((i+1, j+1, i+1, j+2))
                A[i][j] -= 1
                A[i][j+1] += 1

    for i in range(H-1):
        if A[i][W-1] % 2 == 1:
            ans.append((i+1, W, i+2, W))
            A[i][W-1] -= 1
            A[i+1][W-1] += 1

    print(len(ans))
    for a in ans:
        print(*a)

=======

def main():
    H, W = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(H)]
    print(H * W)
    for i in range(H):
        for j in range(W):
            if (i + j) % 2 == 0:
                if j + 1 < W:
                    print(i + 1, j + 1, i + 1, j + 2)
                    a[i][j] -= 1
                    a[i][j + 1] += 1
                else:
                    if i + 1 < H:
                        print(i + 1, j + 1, i + 2, j + 1)
                        a[i][j] -= 1
                        a[i + 1][j] += 1
            else:
                if j + 1 < W:
                    print(i + 1, j + 1, i + 1, j + 2)
                    a[i][j] -= 1
                    a[i][j + 1] += 1
                else:
                    if i + 1 < H:
                        print(i + 1, j + 1, i + 2, j + 1)
                        a[i][j] -= 1
                        a[i + 1][j] += 1
    for i in range(H):
        for j in range(W):
            if a[i][j] % 2 == 1:
                print(i + 1, j + 1, i + 1, j + 1)
                a[i][j] -= 1

=======

def main():
    H, W = map(int, input().split())
    A = []
    for h in range(H):
        A.append(list(map(int, input().split())))
    N = 0
    ans = []
    for h in range(H):
        for w in range(W):
            if A[h][w] % 2 == 1:
                if h != H - 1:
                    ans.append([h + 1, w + 1, h + 2, w + 1])
                    A[h][w] -= 1
                    A[h + 1][w] += 1
                    N += 1
                elif w != W - 1:
                    ans.append([h + 1, w + 1, h + 1, w + 2])
                    A[h][w] -= 1
                    A[h][w + 1] += 1
                    N += 1
    print(N)
    for a in ans:
        print(*a)

=======

def main():
    H,W=map(int,input().split())
    A=[list(map(int,input().split())) for i in range(H)]
    N=0
    ans=[]
    for i in range(H):
        for j in range(W):
            if A[i][j]%2==1:
                if j==W-1 and i<H-1:
                    A[i][j]-=1
                    A[i+1][j]+=1
                    ans.append([i+1,j+1,i+2,j+1])
                elif j<W-1:
                    A[i][j]-=1
                    A[i][j+1]+=1
                    ans.append([i+1,j+1,i+1,j+2])
    print(len(ans))
    for i in range(len(ans)):
        print(*ans[i])

=======

def solve():
    H, W = map(int, input().split())
    A = [[int(i) for i in input().split()] for _ in range(H)]

    # 操作の回数
    N = 0

    # 操作のリスト
    ans = []

    # まずは、縦方向の操作を行う
    for i in range(H):
        for j in range(W-1):
            # 偶数枚のコインが置かれているマスに対しては操作を行わない
            if A[i][j] % 2 == 0:
                continue

            # まだ操作を行っていないマスに対しては、右隣のマスにコインを移動させる
            A[i][j] -= 1
            A[i][j+1] += 1
            N += 1
            ans.append([i+1, j+1, i+1, j+2])

    # 縦方向の操作が終わったら、横方向の操作を行う
    for i in range(H-1):
        # 偶数枚のコインが置かれているマスに対しては操作を行わない
        if A[i][W-1] % 2 == 0:
            continue

        # まだ操作を行っていないマスに対しては、下のマスにコインを移動させる
        A[i][W-1] -= 1
        A[i+1][W-1] += 1
        N += 1
        ans.append([i+1, W, i+2, W])

    # 出力
    print(N)
    for i in ans:
        print(' '.join(map(str, i)))
