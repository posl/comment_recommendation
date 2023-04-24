Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    X = [0] * W
    for j in range(W):
        for i in range(H):
            if C[i][j] == '#':
                X[j] += 1
    print(*X)

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    X = [0] * W
    for i in range(H):
        for j in range(W):
            if C[i][j] == "#":
                X[j] += 1
    print(*X)

=======
Suggestion 3

def main():
    h, w = map(int, input().split())
    c = [input() for _ in range(h)]
    for j in range(w):
        x = 0
        for i in range(h):
            if c[i][j] == '#':
                x += 1
        print(x, end=' ')

main()

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    C = [list(input()) for _ in range(H)]
    X = [0] * W
    for i in range(H):
        for j in range(W):
            if C[i][j] == "#":
                X[j] += 1
    print(*X)

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    grid = [input() for i in range(H)]
    for j in range(W):
        cnt = 0
        for i in range(H):
            if grid[i][j] == '#':
                cnt += 1
        print(cnt, end=' ')

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    c = [list(input()) for _ in range(H)]
    x = [0] * W
    for j in range(W):
        for i in range(H):
            if c[i][j] == "#":
                x[j] += 1
    print(*x)
main()

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    C = []
    for h in range(H):
        C.append(input())
    X = [0] * W
    for w in range(W):
        for h in range(H):
            if C[h][w] == '#':
                X[w] += 1
    print(' '.join(map(str, X)))

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    X = [0] * W
    for _ in range(H):
        for j, C in enumerate(input()):
            if C == "#":
                X[j] += 1
    print(*X)

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    #print(H, W)
    X = [0] * W
    #print(X)
    for i in range(H):
        S = input()
        #print(S)
        for j in range(W):
            if S[j] == "#":
                X[j] += 1
    #print(X)
    print(*X)

=======
Suggestion 10

def main():
    #入力
    H, W = map(int, input().split())
    
    #マスの状態を入力
    C = []
    for i in range(H):
        C.append(input())

    #箱の数を数える
    X = [0] * W
    for i in range(H):
        for j in range(W):
            if C[i][j] == "#":
                X[j] += 1
    
    #出力
    print(*X)
