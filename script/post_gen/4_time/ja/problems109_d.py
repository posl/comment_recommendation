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
                if i == h - 1 and j == w - 1:
                    continue
                elif i == h - 1:
                    a[i][j] -= 1
                    a[i][j + 1] += 1
                    ans.append([i + 1, j + 1, i + 1, j + 2])
                elif j == w - 1:
                    a[i][j] -= 1
                    a[i + 1][j] += 1
                    ans.append([i + 1, j + 1, i + 2, j + 1])
                else:
                    a[i][j] -= 1
                    a[i][j + 1] += 1
                    ans.append([i + 1, j + 1, i + 1, j + 2])
            else:
                continue
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1], ans[i][2], ans[i][3])

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W):
            if i == H-1 and j == W-1:
                break
            if A[i][j] % 2 == 1:
                if j < W-1:
                    ans.append([i+1, j+1, i+1, j+2])
                    A[i][j+1] += 1
                else:
                    ans.append([i+1, j+1, i+2, j+1])
                    A[i+1][j] += 1
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
            if A[i][j] % 2 == 1:
                if j < W - 1:
                    A[i][j] -= 1
                    A[i][j + 1] += 1
                    ans.append((i + 1, j + 1, i + 1, j + 2))
                elif i < H - 1:
                    A[i][j] -= 1
                    A[i + 1][j] += 1
                    ans.append((i + 1, j + 1, i + 2, j + 1))
    print(len(ans))
    for a in ans:
        print(*a)

main()

=======
Suggestion 4

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
        print(*ans[i])

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W):
            if a[i][j] % 2 == 1:
                if j < W - 1:
                    ans.append([i + 1, j + 1, i + 1, j + 2])
                    a[i][j + 1] += 1
                elif i < H - 1:
                    ans.append([i + 1, j + 1, i + 2, j + 1])
                    a[i + 1][j] += 1
    print(len(ans))
    for x in ans:
        print(*x)

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W):
            if i != H - 1:
                if a[i][j] % 2 == 1:
                    a[i][j] -= 1
                    a[i + 1][j] += 1
                    ans.append([i + 1, j + 1, i + 2, j + 1])
            else:
                if j != W - 1:
                    if a[i][j] % 2 == 1:
                        a[i][j] -= 1
                        a[i][j + 1] += 1
                        ans.append([i + 1, j + 1, i + 1, j + 2])
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1], ans[i][2], ans[i][3])

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W):
            if i == H - 1 and j == W - 1:
                continue
            if a[i][j] % 2 == 1:
                if j + 1 < W:
                    a[i][j] -= 1
                    a[i][j + 1] += 1
                    ans.append([i + 1, j + 1, i + 1, j + 2])
                else:
                    a[i][j] -= 1
                    a[i + 1][j] += 1
                    ans.append([i + 1, j + 1, i + 2, j + 1])
    print(len(ans))
    for i in range(len(ans)):
        print(*ans[i])

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    N = 0
    ans = []
    for i in range(H):
        for j in range(W):
            if i == H - 1 and j == W - 1:
                break
            if A[i][j] % 2 == 1:
                N += 1
                if j < W - 1:
                    A[i][j] -= 1
                    A[i][j + 1] += 1
                    ans.append([i + 1, j + 1, i + 1, j + 2])
                else:
                    A[i][j] -= 1
                    A[i + 1][j] += 1
                    ans.append([i + 1, j + 1, i + 2, j + 1])
    print(N)
    for i in range(N):
        print(*ans[i])

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = []

    for i in range(H):
        for j in range(W - 1):
            if A[i][j] % 2 == 1:
                A[i][j] -= 1
                A[i][j + 1] += 1
                ans.append([i + 1, j + 1, i + 1, j + 2])

    for i in range(H - 1):
        if A[i][W - 1] % 2 == 1:
            A[i][W - 1] -= 1
            A[i + 1][W - 1] += 1
            ans.append([i + 1, W, i + 2, W])

    print(len(ans))
    for a in ans:
        print(*a)

=======
Suggestion 10

def main():
    H, W = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(H)]
    b = []
    for i in range(H):
        for j in range(W):
            if a[i][j] % 2 == 1:
                if j == W-1:
                    if i == H-1:
                        pass
                    else:
                        b.append([i+1, j+1, i+2, j+1])
                        a[i+1][j] += 1
                else:
                    b.append([i+1, j+1, i+1, j+2])
                    a[i][j+1] += 1
    print(len(b))
    for i in range(len(b)):
        print(b[i][0], b[i][1], b[i][2], b[i][3])
