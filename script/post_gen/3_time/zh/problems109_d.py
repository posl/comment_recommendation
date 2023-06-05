Synthesizing 10/10 solutions

=======
Suggestion 1

def printAns(ans):
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i][0],ans[i][1],ans[i][2],ans[i][3])

=======
Suggestion 2

def func(h, w, a):
    n = 0
    ans = []
    for i in range(h):
        for j in range(w):
            if a[i][j]%2 == 1 and j != w-1:
                a[i][j] -= 1
                a[i][j+1] += 1
                n += 1
                ans.append([i+1, j+1, i+1, j+2])
            elif a[i][j]%2 == 1 and i != h-1:
                a[i][j] -= 1
                a[i+1][j] += 1
                n += 1
                ans.append([i+1, j+1, i+2, j+1])
    print(n)
    for i in range(n):
        print(ans[i][0], ans[i][1], ans[i][2], ans[i][3])

=======
Suggestion 3

def solve():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    ans = []
    for i in range(h):
        for j in range(w):
            if i % 2 == 0:
                if j == w - 1:
                    if a[i][j] % 2 == 1:
                        a[i][j] -= 1
                        a[i + 1][j] += 1
                        ans.append((i + 1, j + 1, i + 2, j + 1))
                else:
                    if a[i][j] % 2 == 1:
                        a[i][j] -= 1
                        a[i][j + 1] += 1
                        ans.append((i + 1, j + 1, i + 1, j + 2))
            else:
                if j == 0:
                    if a[i][j] % 2 == 1:
                        a[i][j] -= 1
                        a[i + 1][j] += 1
                        ans.append((i + 1, j + 1, i + 2, j + 1))
                else:
                    if a[i][j] % 2 == 1:
                        a[i][j] -= 1
                        a[i][j - 1] += 1
                        ans.append((i + 1, j + 1, i + 1, j))
    print(len(ans))
    for i in range(len(ans)):
        print(*ans[i])

=======
Suggestion 4

def check_even(h,w,board):
    even_count = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] % 2 == 0:
                even_count += 1
    return even_count

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
            if a[i][j] % 2 != 0:
                if j < w - 1:
                    a[i][j + 1] += 1
                    ans.append([i + 1, j + 1, i + 1, j + 2])
                elif i < h - 1:
                    a[i + 1][j] += 1
                    ans.append([i + 1, j + 1, i + 2, j + 1])

    print(len(ans))
    for i in range(len(ans)):
        print(*ans[i])

=======
Suggestion 6

def print_operation(operation):
    print(len(operation))
    for o in operation:
        print(o[0],o[1],o[2],o[3])

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W):
            if a[i][j] % 2 == 1:
                if j < W - 1:
                    a[i][j] -= 1
                    a[i][j + 1] += 1
                    ans.append([i + 1, j + 1, i + 1, j + 2])
                elif i < H - 1:
                    a[i][j] -= 1
                    a[i + 1][j] += 1
                    ans.append([i + 1, j + 1, i + 2, j + 1])
    print(len(ans))
    for i in range(len(ans)):
        print(*ans[i])

=======
Suggestion 8

def solve(h, w, a):
    ans = []
    for i in range(h):
        if i % 2 == 0:
            for j in range(w - 1):
                if a[i][j] % 2 == 1:
                    a[i][j] -= 1
                    a[i][j + 1] += 1
                    ans.append([i + 1, j + 1, i + 1, j + 2])
            if i != h - 1 and a[i][w - 1] % 2 == 1:
                a[i][w - 1] -= 1
                a[i + 1][w - 1] += 1
                ans.append([i + 1, w, i + 2, w])
        else:
            for j in range(w - 1, 0, -1):
                if a[i][j] % 2 == 1:
                    a[i][j] -= 1
                    a[i][j - 1] += 1
                    ans.append([i + 1, j + 1, i + 1, j])
            if i != h - 1 and a[i][0] % 2 == 1:
                a[i][0] -= 1
                a[i + 1][0] += 1
                ans.append([i + 1, 1, i + 2, 1])
    print(len(ans))
    for i in ans:
        print(*i)

h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
solve(h, w, a)

=======
Suggestion 9

def main():
    pass

=======
Suggestion 10

def main():
    H, W = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(H)]
    N = 0
    ans = []
    for i in range(H):
        for j in range(W):
            if a[i][j] % 2 == 1:
                if j < W - 1:
                    a[i][j + 1] += 1
                    ans.append([i + 1, j + 1, i + 1, j + 2])
                    N += 1
                elif i < H - 1:
                    a[i + 1][j] += 1
                    ans.append([i + 1, j + 1, i + 2, j + 1])
                    N += 1
    print(N)
    for i in range(N):
        print(ans[i][0], ans[i][1], ans[i][2], ans[i][3])
main()
