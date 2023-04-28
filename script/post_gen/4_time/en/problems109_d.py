Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W):
            if A[i][j] % 2 == 0:
                continue
            if j == W - 1 and i == H - 1:
                break
            if j == W - 1:
                A[i + 1][j] += 1
                ans.append([i + 1, j + 1, i + 2, j + 1])
            else:
                A[i][j + 1] += 1
                ans.append([i + 1, j + 1, i + 1, j + 2])
    print(len(ans))
    for a in ans:
        print(' '.join(map(str, a)))

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W):
            if A[i][j] % 2 == 1:
                if j + 1 < W:
                    A[i][j] -= 1
                    A[i][j + 1] += 1
                    ans.append([i + 1, j + 1, i + 1, j + 2])
                elif i + 1 < H:
                    A[i][j] -= 1
                    A[i + 1][j] += 1
                    ans.append([i + 1, j + 1, i + 2, j + 1])
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
        for j in range(W):
            if i % 2 == 0:
                if j % 2 == 0:
                    if A[i][j] % 2 == 1:
                        if j < W - 1:
                            ans.append([i + 1, j + 1, i + 1, j + 2])
                            A[i][j + 1] += 1
                        elif i < H - 1:
                            ans.append([i + 1, j + 1, i + 2, j + 1])
                            A[i + 1][j] += 1
                else:
                    if A[i][j] % 2 == 1:
                        if i < H - 1:
                            ans.append([i + 1, j + 1, i + 2, j + 1])
                            A[i + 1][j] += 1
                        elif j < W - 1:
                            ans.append([i + 1, j + 1, i + 1, j + 2])
                            A[i][j + 1] += 1
            else:
                if j % 2 == 0:
                    if A[i][j] % 2 == 1:
                        if j < W - 1:
                            ans.append([i + 1, j + 1, i + 1, j + 2])
                            A[i][j + 1] += 1
                        elif i > 0:
                            ans.append([i + 1, j + 1, i, j + 1])
                            A[i - 1][j] += 1
                else:
                    if A[i][j] % 2 == 1:
                        if i > 0:
                            ans.append([i + 1, j + 1, i, j + 1])
                            A[i - 1][j] += 1
                        elif j < W - 1:
                            ans.append([i + 1, j + 1, i + 1, j + 2])
                            A[i][j + 1] +=

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for h in range(H):
        for w in range(W):
            if A[h][w] % 2 == 1:
                if w + 1 < W:
                    ans.append((h, w, h, w + 1))
                    A[h][w + 1] += 1
                elif h + 1 < H:
                    ans.append((h, w, h + 1, w))
                    A[h + 1][w] += 1
    print(len(ans))
    for h, w, h1, w1 in ans:
        print(h + 1, w + 1, h1 + 1, w1 + 1)

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W-1):
            if A[i][j] % 2:
                A[i][j] -= 1
                A[i][j+1] += 1
                ans.append((i, j, i, j+1))
    for i in range(H-1):
        if A[i][W-1] % 2:
            A[i][W-1] -= 1
            A[i+1][W-1] += 1
            ans.append((i, W-1, i+1, W-1))
    print(len(ans))
    for a in ans:
        print(*[a[i]+1 for i in range(4)])

=======
Suggestion 6

def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    ans = []
    for i in range(h):
        for j in range(w-1):
            if a[i][j] % 2 == 1:
                a[i][j] -= 1
                a[i][j+1] += 1
                ans.append((i+1, j+1, i+1, j+2))
    for i in range(h-1):
        if a[i][-1] % 2 == 1:
            a[i][-1] -= 1
            a[i+1][-1] += 1
            ans.append((i+1, w, i+2, w))
    print(len(ans))
    for i, j, k, l in ans:
        print(i, j, k, l)

=======
Suggestion 7

def solve():
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
    for i in ans:
        print(*i)

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = []

    for h in range(H):
        for w in range(W):
            if A[h][w] % 2 == 0:
                continue
            if w + 1 < W:
                ans.append((h + 1, w + 1, h + 1, w + 2))
                A[h][w + 1] += 1
            elif h + 1 < H:
                ans.append((h + 1, w + 1, h + 2, w + 1))
                A[h + 1][w] += 1
    print(len(ans))
    for a in ans:
        print(*a)

=======
Suggestion 9

def get_input():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    return h, w, a

=======
Suggestion 10

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    # H, W = 500, 500
    # A = [[9] * W for _ in range(H)]

    N = 0
    ans = []
    for i in range(H):
        for j in range(W):
            if A[i][j] % 2:
                if j + 1 < W:
                    A[i][j] -= 1
                    A[i][j + 1] += 1
                    ans.append((i + 1, j + 1, i + 1, j + 2))
                    N += 1
                elif i + 1 < H:
                    A[i][j] -= 1
                    A[i + 1][j] += 1
                    ans.append((i + 1, j + 1, i + 2, j + 1))
                    N += 1

    print(N)
    for a in ans:
        print(*a)
