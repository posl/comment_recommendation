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
                    ans.append((i + 1, j + 1, i + 1, j + 2))
                elif i < h - 1:
                    a[i][j] -= 1
                    a[i + 1][j] += 1
                    ans.append((i + 1, j + 1, i + 2, j + 1))
    print(len(ans))
    for y1, x1, y2, x2 in ans:
        print(y1, x1, y2, x2)

main()

=======
Suggestion 2

def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    ans = []
    for i in range(h):
        for j in range(w):
            if a[i][j] % 2 == 1:
                if j == w - 1:
                    if i != h - 1:
                        a[i][j] -= 1
                        a[i + 1][j] += 1
                        ans.append([i + 1, j + 1, i + 2, j + 1])
                else:
                    a[i][j] -= 1
                    a[i][j + 1] += 1
                    ans.append([i + 1, j + 1, i + 1, j + 2])
    print(len(ans))
    for i in range(len(ans)):
        for j in range(4):
            print(ans[i][j], end=" ")
        print()

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
    for y1, x1, y2, x2 in ans:
        print(y1, x1, y2, x2)

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W):
            if a[i][j] % 2 == 1:
                if j == W - 1:
                    if i < H - 1:
                        a[i][j] -= 1
                        a[i + 1][j] += 1
                        ans.append([i + 1, j + 1, i + 2, j + 1])
                else:
                    a[i][j] -= 1
                    a[i][j + 1] += 1
                    ans.append([i + 1, j + 1, i + 1, j + 2])
    print(len(ans))
    for i in ans:
        print(*i)

=======
Suggestion 5

def solve():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W):
            if A[i][j] % 2 == 1:
                if i == H - 1 and j == W - 1:
                    pass
                elif i == H - 1:
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
solve()

=======
Suggestion 6

def solve():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W):
            if A[i][j] % 2 == 1:
                if j == W-1 and i != H-1:
                    A[i][j] -= 1
                    A[i+1][j] += 1
                    ans.append((i+1, j+1, i+2, j+1))
                elif j != W-1:
                    A[i][j] -= 1
                    A[i][j+1] += 1
                    ans.append((i+1, j+1, i+1, j+2))
    print(len(ans))
    for a in ans:
        print(*a)

=======
Suggestion 7

def solve():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for h in range(H):
        for w in range(W):
            if A[h][w] % 2 == 1:
                if h == H-1 and w == W-1:
                    continue
                elif w == W-1:
                    ans.append([h+1, w+1, h+2, w+1])
                    A[h+1][w] += 1
                else:
                    ans.append([h+1, w+1, h+1, w+2])
                    A[h][w+1] += 1
    print(len(ans))
    for a in ans:
        print(*a)

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    # 偶数枚のコインが置かれたマスの数を最大化
    # まず、偶数枚のコインが置かれたマスの数を数える。
    # 次に、操作を行い、偶数枚のコインが置かれたマスの数を最大化する。
    # 1. まず、偶数枚のコインが置かれたマスの数を数える。
    ans = 0
    for i in range(H):
        for j in range(W):
            if A[i][j] % 2 == 0:
                ans += 1

    # 2. 次に、操作を行い、偶数枚のコインが置かれたマスの数を最大化する。
    # まず、偶数枚のコインが置かれたマスの数を数える。
    # 次に、操作を行い、偶数枚のコインが置かれたマスの数を最大化する。
    # 1. まず、偶数枚のコインが置かれたマスの数を数える。
    ans = 0
    for i in range(H):
        for j in range(W):
            if A[i][j] % 2 == 0:
                ans += 1

    # 2. 次に、操作を行い、偶数枚のコインが置かれたマスの数を最大化する。
    # まず、偶数枚のコインが置かれたマスの数を数える。
    # 次に、操作を行い、偶数枚のコインが置かれたマスの数を最大化する。
    # 1. まず、偶数枚のコインが置かれたマスの数を数える

=======
Suggestion 9

def main():
    H, W = [int(x) for x in input().split()]
    A = [[int(x) for x in input().split()] for _ in range(H)]
    N = 0
    moves = []
    for i in range(H):
        for j in range(W):
            if A[i][j] % 2 == 1:
                if j < W - 1:
                    A[i][j] -= 1
                    A[i][j + 1] += 1
                    moves.append((i + 1, j + 1, i + 1, j + 2))
                    N += 1
                elif i < H - 1:
                    A[i][j] -= 1
                    A[i + 1][j] += 1
                    moves.append((i + 1, j + 1, i + 2, j + 1))
                    N += 1
    print(N)
    for move in moves:
        print(*move)

=======
Suggestion 10

def  main ():
    h, w = map( int , input().split())
    a = [ list (map( int , input().split())) for  _  in  range (h)]
    ans = []
     for  i  in  range (h):
         for  j  in  range (w):
             if  a[i][j] % 2:
                a[i][j] -= 1
                 if  i < h - 1:
                    a[i + 1][j] += 1
                    ans.append([i + 1, j + 1, i + 2, j + 1])
                 elif  j < w - 1:
                    a[i][j + 1] += 1
                    ans.append([i + 1, j + 1, i + 1, j + 2])
    print ( len (ans))
     for  i  in  ans:
        print ( ' ' .join(map( str , i)))
