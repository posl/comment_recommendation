Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    print('hello world')

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W):
            if a[i][j] % 2 == 1:
                if j < W - 1:
                    a[i][j + 1] += 1
                    ans.append([i + 1, j + 1, i + 1, j + 2])
                else:
                    if i < H - 1:
                        a[i + 1][j] += 1
                        ans.append([i + 1, j + 1, i + 2, j + 1])
    print(len(ans))
    for i in range(len(ans)):
        print(*ans[i])

=======
Suggestion 4

def even(a):
    if a % 2 == 0:
        return True
    else:
        return False

=======
Suggestion 5

def main():
    H,W = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W):
            if a[i][j]%2 == 1:
                if j < W-1:
                    a[i][j] -= 1
                    a[i][j+1] += 1
                    ans.append([i+1,j+1,i+1,j+2])
                elif i < H-1:
                    a[i][j] -= 1
                    a[i+1][j] += 1
                    ans.append([i+1,j+1,i+2,j+1])
    print(len(ans))
    for i in ans:
        print(*i)

=======
Suggestion 6

def main():
    h,w = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(h)]
    ans = []
    for i in range(h):
        for j in range(w):
            if i%2 == 0:
                if a[i][j]%2 == 1:
                    if j != w-1:
                        a[i][j] -= 1
                        a[i][j+1] += 1
                        ans.append([i+1,j+1,i+1,j+2])
                    elif i != h-1:
                        a[i][j] -= 1
                        a[i+1][j] += 1
                        ans.append([i+1,j+1,i+2,j+1])
            else:
                if a[i][w-1-j]%2 == 1:
                    if j != w-1:
                        a[i][w-1-j] -= 1
                        a[i][w-1-j-1] += 1
                        ans.append([i+1,w-j,i+1,w-j-1])
                    elif i != h-1:
                        a[i][w-1-j] -= 1
                        a[i+1][w-1-j] += 1
                        ans.append([i+1,w-j,i+2,w-j])
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i][0],ans[i][1],ans[i][2],ans[i][3])

=======
Suggestion 7

def main():
    h,w = map(int,input().split())
    a = [list(map(int,input().split())) for i in range(h)]
    ans = []
    for i in range(h):
        for j in range(w):
            if a[i][j]%2 == 1:
                if j != w-1:
                    a[i][j] -= 1
                    a[i][j+1] += 1
                    ans.append([i+1,j+1,i+1,j+2])
                elif i != h-1:
                    a[i][j] -= 1
                    a[i+1][j] += 1
                    ans.append([i+1,j+1,i+2,j+1])
    print(len(ans))
    for i in range(len(ans)):
        print(*ans[i])

=======
Suggestion 8

def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(h)]
    ans = []
    for i in range(h):
        for j in range(w):
            if a[i][j] % 2 == 1:
                if j < w - 1:
                    a[i][j + 1] += 1
                    ans.append([i + 1, j + 1, i + 1, j + 2])
                else:
                    if i < h - 1:
                        a[i + 1][j] += 1
                        ans.append([i + 1, j + 1, i + 2, j + 1])
    print(len(ans))
    for i in range(len(ans)):
        print(" ".join(map(str, ans[i])))
