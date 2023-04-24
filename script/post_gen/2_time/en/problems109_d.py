Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W):
            if (i+j) % 2 == 1 and A[i][j] % 2 == 1:
                if j+1 < W:
                    ans.append((i+1, j+1, i+1, j+2))
                    A[i][j+1] += 1
                elif i+1 < H:
                    ans.append((i+1, j+1, i+2, j+1))
                    A[i+1][j] += 1
    for i in range(H):
        for j in range(W-1):
            if A[i][j] % 2 == 1:
                ans.append((i+1, j+1, i+1, j+2))
                A[i][j+1] += 1
    print(len(ans))
    for a in ans:
        print(*a)

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W):
            if i % 2 == 0 and j != W - 1:
                if A[i][j] % 2 == 1:
                    ans.append((i + 1, j + 1, i + 1, j + 2))
                    A[i][j + 1] += 1
            elif i % 2 == 0 and j == W - 1:
                if i != H - 1 and A[i][j] % 2 == 1:
                    ans.append((i + 1, j + 1, i + 2, j + 1))
                    A[i + 1][j] += 1
            elif i % 2 == 1 and j != 0:
                if A[i][j] % 2 == 1:
                    ans.append((i + 1, j + 1, i + 1, j))
                    A[i][j - 1] += 1
            elif i % 2 == 1 and j == 0:
                if i != H - 1 and A[i][j] % 2 == 1:
                    ans.append((i + 1, j + 1, i + 2, j + 1))
                    A[i + 1][j] += 1
    print(len(ans))
    for a in ans:
        print(*a)

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W-1):
            if A[i][j] % 2 == 1:
                A[i][j] -= 1
                A[i][j+1] += 1
                ans.append([i+1, j+1, i+1, j+2])
    for i in range(H-1):
        if A[i][W-1] % 2 == 1:
            A[i][W-1] -= 1
            A[i+1][W-1] += 1
            ans.append([i+1, W, i+2, W])
    print(len(ans))
    for i in ans:
        print(*i)

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    ans = []
    for i in range(H):
        for j in range(W):
            if A[i][j] % 2 == 0:
                continue
            if j != W - 1:
                A[i][j] -= 1
                A[i][j + 1] += 1
                ans.append((i + 1, j + 1, i + 1, j + 2))
            elif i != H - 1:
                A[i][j] -= 1
                A[i + 1][j] += 1
                ans.append((i + 1, j + 1, i + 2, j + 1))

    print(len(ans))
    for a in ans:
        print(*a)

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    ans = []
    for h in range(H):
        for w in range(W):
            if h % 2 == 0:
                if w == W - 1:
                    if h == H - 1:
                        continue
                    if A[h][w] % 2 == 1:
                        A[h + 1][w] += 1
                        ans.append((h + 1, w + 1, h + 2, w + 1))
                else:
                    if A[h][w] % 2 == 1:
                        A[h][w + 1] += 1
                        ans.append((h + 1, w + 1, h + 1, w + 2))
            else:
                if w == 0:
                    if A[h][w] % 2 == 1:
                        A[h + 1][w] += 1
                        ans.append((h + 1, w + 1, h + 2, w + 1))
                else:
                    if A[h][w] % 2 == 1:
                        A[h][w - 1] += 1
                        ans.append((h + 1, w + 1, h + 1, w))

    print(len(ans))
    for a in ans:
        print(*a)

=======
Suggestion 6

def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(h)]
    ans = []
    for i in range(h):
        for j in range(w - 1):
            if a[i][j] % 2 == 1:
                a[i][j] -= 1
                a[i][j + 1] += 1
                ans.append((i + 1, j + 1, i + 1, j + 2))
    for i in range(h - 1):
        if a[i][w - 1] % 2 == 1:
            a[i][w - 1] -= 1
            a[i + 1][w - 1] += 1
            ans.append((i + 1, w, i + 2, w))
    print(len(ans))
    for y1, x1, y2, x2 in ans:
        print(y1, x1, y2, x2)

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    N = 0
    ans = []
    for h in range(H):
        for w in range(W):
            if A[h][w] % 2 == 0:
                continue
            if w + 1 < W:
                A[h][w] -= 1
                A[h][w + 1] += 1
                N += 1
                ans.append([h + 1, w + 1, h + 1, w + 2])
            elif h + 1 < H:
                A[h][w] -= 1
                A[h + 1][w] += 1
                N += 1
                ans.append([h + 1, w + 1, h + 2, w + 1])

    print(N)
    for a in ans:
        print(*a)

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    print(H*W-1)
    for i in range(H):
        for j in range(W):
            if j < W-1:
                if A[i][j] % 2 == 1:
                    print(i+1, j+1, i+1, j+2)
                    A[i][j+1] += 1
            else:
                if A[i][j] % 2 == 1 and i < H-1:
                    print(i+1, j+1, i+2, j+1)
                    A[i+1][j] += 1

=======
Suggestion 9

def solve(h, w, A):
    ans = []
    for i in range(h):
        for j in range(w):
            if i%2 == 0:
                if j == w-1:
                    if i == h-1:
                        break
                    else:
                        if A[i+1][j]%2 == 1:
                            ans.append([i+1, j+1, i+2, j+1])
                            A[i+1][j] -= 1
                else:
                    if A[i][j+1]%2 == 1:
                        ans.append([i+1, j+1, i+1, j+2])
                        A[i][j+1] -= 1
            else:
                if j == 0:
                    if A[i+1][j]%2 == 1:
                        ans.append([i+1, j+1, i+2, j+1])
                        A[i+1][j] -= 1
                else:
                    if A[i][j-1]%2 == 1:
                        ans.append([i+1, j+1, i+1, j])
                        A[i][j-1] -= 1
    return ans

h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]
ans = solve(h, w, A)
print(len(ans))
for a in ans:
    print(*a)

=======
Suggestion 10

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    # N: number of operations
    N = 0
    # ops: operations
    ops = []

    # for each row
    for i in range(H):
        # for each column
        for j in range(W):
            # if the number of coins is odd
            if A[i][j] % 2 == 1:
                # if the cell is not the last cell in the row
                if j < W - 1:
                    # move one coin to the right
                    A[i][j] -= 1
                    A[i][j + 1] += 1
                    N += 1
                    ops.append((i + 1, j + 1, i + 1, j + 2))
                # if the cell is the last cell in the row
                else:
                    # move one coin to the bottom
                    A[i][j] -= 1
                    A[i + 1][j] += 1
                    N += 1
                    ops.append((i + 1, j + 1, i + 2, j + 1))

    # output
    print(N)
    for op in ops:
        print(*op)
