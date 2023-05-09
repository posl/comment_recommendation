Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    ans = []
    for i in range(h):
        for j in range(w):
            if a[i][j] % 2 == 1:
                if j < w - 1:
                    a[i][j] -= 1
                    a[i][j + 1] += 1
                    ans.append([i + 1, j + 1, i + 1, j + 2])
                elif i < h - 1:
                    a[i][j] -= 1
                    a[i + 1][j] += 1
                    ans.append([i + 1, j + 1, i + 2, j + 1])
    print(len(ans))
    for i in range(len(ans)):
        print(' '.join(map(str, ans[i])))

=======
Suggestion 2

def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    ans = []
    for i in range(h):
        for j in range(w-1):
            if a[i][j] % 2 == 1:
                a[i][j+1] += 1
                ans.append([i+1, j+1, i+1, j+2])
    for i in range(h-1):
        if a[i][w-1] % 2 == 1:
            a[i+1][w-1] += 1
            ans.append([i+1, w, i+2, w])
    print(len(ans))
    for i in range(len(ans)):
        print(*ans[i])

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W):
            if A[i][j] % 2 == 1:
                if j < W - 1:
                    A[i][j] -= 1
                    A[i][j+1] += 1
                    ans.append((i+1, j+1, i+1, j+2))
                elif i < H - 1:
                    A[i][j] -= 1
                    A[i+1][j] += 1
                    ans.append((i+1, j+1, i+2, j+1))
    print(len(ans))
    for i in ans:
        print(*i)

=======
Suggestion 4

def main():
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))

    ans = []
    for i in range(h):
        for j in range(w):
            if i == h-1 and j == w-1:
                break
            if a[i][j] % 2 == 1:
                if j == w-1:
                    a[i+1][j] += 1
                    ans.append((i+1, j+1, i+2, j+1))
                else:
                    a[i][j+1] += 1
                    ans.append((i+1, j+1, i+1, j+2))
    print(len(ans))
    for i in ans:
        print(*i)

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    ret = []
    for y in range(h):
        for x in range(w):
            if a[y][x] % 2 == 1:
                if x < w-1:
                    a[y][x+1] += 1
                    ret.append((y+1, x+1, y+1, x+2))
                elif y < h-1:
                    a[y+1][x] += 1
                    ret.append((y+1, x+1, y+2, x+1))
    print(len(ret))
    for y1, x1, y2, x2 in ret:
        print(y1, x1, y2, x2)

=======
Suggestion 6

def get_input():
    H, W = map(int, input().strip().split())
    A = []
    for _ in range(H):
        A.append(list(map(int, input().strip().split())))
    return H, W, A

=======
Suggestion 7

def main():
    # input
    H, W = map(int, input().split())
    a = []
    for i in range(H):
        a.append(list(map(int, input().split())))
    # solve
    ans = []
    for i in range(H):
        for j in range(W-1):
            if a[i][j] % 2 == 1:
                a[i][j+1] += 1
                ans.append([i+1, j+1, i+1, j+2])
    for i in range(H-1):
        if a[i][W-1] % 2 == 1:
            a[i+1][W-1] += 1
            ans.append([i+1, W, i+2, W])
    # output
    print(len(ans))
    for i in range(len(ans)):
        print(' '.join(map(str, ans[i])))

=======
Suggestion 8

def print_move(y, x, y_to, x_to):
    print("{0} {1} {2} {3}".format(y, x, y_to, x_to))

=======
Suggestion 9

def move_coin(y, x, y_, x_):
    print(y, x, y_, x_)

=======
Suggestion 10

def main():
    pass
