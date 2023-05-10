Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H)]
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
        print(*a)

=======
Suggestion 2

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
                elif i < H - 1:
                    A[i][j] -= 1
                    A[i + 1][j] += 1
                    ans.append([i + 1, j + 1, i + 2, j + 1])
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1], ans[i][2], ans[i][3])

main()

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W):
            if A[i][j] % 2 == 1:
                if j < W-1:
                    ans.append([i+1, j+1, i+1, j+2])
                    A[i][j+1] += 1
                else:
                    if i < H-1:
                        ans.append([i+1, j+1, i+2, j+1])
                        A[i+1][j] += 1
    print(len(ans))
    for i in range(len(ans)):
        print(*ans[i])

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(H)]
    ans = []
    for i in range(H):
        for j in range(W):
            if A[i][j] % 2 == 1:
                if j < W - 1:
                    A[i][j + 1] += 1
                    ans.append([i + 1, j + 1, i + 1, j + 2])
                elif i < H - 1:
                    A[i + 1][j] += 1
                    ans.append([i + 1, j + 1, i + 2, j + 1])
    print(len(ans))
    for i in range(len(ans)):
        print(*ans[i])

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    ans = []
    for i in range(h):
        for j in range(w):
            if a[i][j] % 2 == 1:
                if j < w-1:
                    a[i][j+1] += 1
                    ans.append([i+1, j+1, i+1, j+2])
                elif i < h-1:
                    a[i+1][j] += 1
                    ans.append([i+1, j+1, i+2, j+1])
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1], ans[i][2], ans[i][3])

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    A = [[int(x) for x in input().split()] for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W):
            if A[i][j] % 2 == 1:
                if j < W - 1:
                    ans.append([i + 1, j + 1, i + 1, j + 2])
                    A[i][j + 1] += 1
                    A[i][j] -= 1
                elif i < H - 1:
                    ans.append([i + 1, j + 1, i + 2, j + 1])
                    A[i + 1][j] += 1
                    A[i][j] -= 1
    print(len(ans))
    for i in range(len(ans)):
        print(*ans[i])

=======
Suggestion 7

def solve():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    ans = []
    for i in range(h):
        for j in range(w):
            if a[i][j] % 2 == 1:
                if j != w - 1:
                    a[i][j + 1] += 1
                    ans.append((i + 1, j + 1, i + 1, j + 2))
                elif i != h - 1:
                    a[i + 1][j] += 1
                    ans.append((i + 1, j + 1, i + 2, j + 1))
    print(len(ans))
    for i in range(len(ans)):
        print(*ans[i])
solve()

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W):
            if i == H - 1 and j == W - 1:
                continue
            if A[i][j] % 2 == 1:
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
Suggestion 9

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
                elif i < H - 1:
                    A[i][j] -= 1
                    A[i + 1][j] += 1
                    ans.append([i + 1, j + 1, i + 2, j + 1])
    print(len(ans))
    for a in ans:
        print(*a)

=======
Suggestion 10

def move_coin(h1,w1,h2,w2):
    print(h1,w1,h2,w2)
    return
