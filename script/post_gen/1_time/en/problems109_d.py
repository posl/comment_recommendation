Synthesizing 9/10 solutions

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
            if j < W - 1:
                A[i][j] -= 1
                A[i][j + 1] += 1
                ans.append((i + 1, j + 1, i + 1, j + 2))
            elif i < H - 1:
                A[i][j] -= 1
                A[i + 1][j] += 1
                ans.append((i + 1, j + 1, i + 2, j + 1))
    print(len(ans))
    for x in ans:
        print(*x)

=======
Suggestion 2

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
            else:
                pass
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i][0] + 1, ans[i][1] + 1, ans[i][2] + 1, ans[i][3] + 1)

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    for i in range(H):
        for j in range(W):
            if a[i][j] % 2 == 0:
                continue
            if j + 1 < W:
                ans.append((i + 1, j + 1, i + 1, j + 2))
                a[i][j + 1] += 1
            elif i + 1 < H:
                ans.append((i + 1, j + 1, i + 2, j + 1))
                a[i + 1][j] += 1
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
            if A[i][j] % 2 == 1:
                if j + 1 < W:
                    ans.append((i, j, i, j + 1))
                    A[i][j] -= 1
                    A[i][j + 1] += 1
                elif i + 1 < H:
                    ans.append((i, j, i + 1, j))
                    A[i][j] -= 1
                    A[i + 1][j] += 1

    print(len(ans))
    for i, j, k, l in ans:
        print(i + 1, j + 1, k + 1, l + 1)

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    ans = []
    for i in range(H):
        for j in range(W - 1):
            if A[i][j] % 2 == 1:
                A[i][j] -= 1
                A[i][j + 1] += 1
                ans.append((i + 1, j + 1, i + 1, j + 2))

    for i in range(H - 1):
        if A[i][W - 1] % 2 == 1:
            A[i][W - 1] -= 1
            A[i + 1][W - 1] += 1
            ans.append((i + 1, W, i + 2, W))

    print(len(ans))
    for a in ans:
        print(*a)

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(H)]

    ans = []
    for i in range(H):
        for j in range(W):
            if a[i][j] % 2 == 0:
                continue

            if j + 1 < W:
                ans.append((i, j, i, j + 1))
                a[i][j] -= 1
                a[i][j + 1] += 1
            elif i + 1 < H:
                ans.append((i, j, i + 1, j))
                a[i][j] -= 1
                a[i + 1][j] += 1

    print(len(ans))
    for y, x, y2, x2 in ans:
        print(y + 1, x + 1, y2 + 1, x2 + 1)

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    A = [[int(a) for a in input().split()] for _ in range(H)]
    ans = []
    for h in range(H):
        for w in range(W):
            if h % 2 == 0:
                if w < W - 1:
                    if A[h][w] % 2 == 1:
                        A[h][w] -= 1
                        A[h][w + 1] += 1
                        ans.append((h + 1, w + 1, h + 1, w + 2))
            else:
                if w > 0:
                    if A[h][w] % 2 == 1:
                        A[h][w] -= 1
                        A[h][w - 1] += 1
                        ans.append((h + 1, w + 1, h + 1, w))
    print(len(ans))
    for a in ans:
        print(*a)

=======
Suggestion 8

def main():
    H, W = [int(x) for x in input().split()]
    a = [list(input().split()) for _ in range(H)]
    N = 0
    ans = []
    for i in range(H):
        for j in range(W):
            if int(a[i][j]) % 2 == 1:
                if j < W - 1:
                    ans.append([i + 1, j + 1, i + 1, j + 2])
                    N += 1
                elif i < H - 1:
                    ans.append([i + 1, j + 1, i + 2, j + 1])
                    N += 1
    print(N)
    for i in range(N):
        print(" ".join([str(x) for x in ans[i]]))

=======
Suggestion 9

def even ( x ) : return x % 2 == 0 def odd ( x ) : return x % 2 == 1 def main ( ) : H , W = map ( int , input ( ) . split ( ) ) A = [ list ( map ( int , input ( ) . split ( ) ) ) for _ in range ( H ) ] N = 0 ans = [ ] for h in range ( H - 1 ) : for w in range ( W ) : if odd ( A [ h ] [ w ] ) : A [ h ] [ w ] -= 1 A [ h + 1 ] [ w ] += 1 N += 1 ans . append ( ( h + 1 , w + 1 , h + 2 , w + 1 ) ) for w in range ( W - 1 ) : if odd ( A [ H - 1 ] [ w ] ) : A [ H - 1 ] [ w ] -= 1 A [ H - 1 ] [ w + 1 ] += 1 N += 1 ans . append ( ( H , w + 1 , H , w + 2 ) ) print ( N ) for a in ans : print ( ' ' . join ( map ( str , a ) ) ) if __name__ == '__main__' : main ( )
