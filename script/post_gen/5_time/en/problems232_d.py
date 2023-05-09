Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    C = [input() for i in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if C[i][j] == '.':
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    C = [list(input()) for i in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if C[i][j] == '.':
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    h, w = map(int, input().split())
    s = [input() for i in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '.':
                count += 1
    print(count)

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if i % 2 == 0:
                if C[i][j] == '.':
                    ans += 1
            else:
                if C[i][W-j-1] == '.':
                    ans += 1
    print(ans)

=======
Suggestion 5

def get_input():
    H, W = map(int, input().split())
    grid = []
    for i in range(H):
        grid.append(list(input()))
    return H, W, grid

=======
Suggestion 6

def main():
    # Take input Here and Call solution function
    h, w = get_ints_in_variables()
    matrix = []
    for i in range(h):
        matrix.append(get_string())

    print(solution(h, w, matrix))

=======
Suggestion 7

def main():
    h, w = map(int, input().split())
    c = [input() for _ in range(h)]
    print(sum([1 for i in range(h) for j in range(w) if c[i][j] == '.']))

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    print(H * W - sum(s.count('#') for s in S))

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    grid = [list(input()) for _ in range(H)]
    #print(grid)
    #print(grid[0][0])
    #print(grid[0][1])
    #print(grid[1][0])
    #print(grid[1][1])
    #print(grid[1][2])
    #print(grid[2][2])
    #print(grid[2][3])
    #print(grid[3][3])
    #print(grid[3][4])
    #print(grid[4][4])
    #print(grid[4][5])
    #print(grid[4][6])

    #print(grid[0][0])
    #print(grid[0][1])
    #print(grid[1][0])
    #print(grid[1][1])
    #print(grid[1][2])
    #print(grid[2][2])
    #print(grid[2][3])
    #print(grid[3][3])
    #print(grid[3][4])
    #print(grid[4][4])
    #print(grid[4][5])
    #print(grid[4][6])

    #print(grid[0][0])
    #print(grid[0][1])
    #print(grid[1][0])
    #print(grid[1][1])
    #print(grid[1][2])
    #print(grid[2][2])
    #print(grid[2][3])
    #print(grid[3][3])
    #print(grid[3][4])
    #print(grid[4][4])
    #print(grid[4][5])
    #print(grid[4][6])

    #print(grid[0][0])
    #print(grid[0][1])
    #print(grid[1][0])
    #print(grid[1][1])
    #print(grid[1][2])
    #print(grid[2][2])
    #print(grid[2][3])
    #print(grid[3][3])
    #print(grid[3][4])
    #print(grid[4][4])
    #print(grid[4][5])
    #print(grid[4][6])

    #print(grid[0][0])
    #print(grid[0][1])
    #print(grid[1][0])
    #print(grid[1][1])

=======
Suggestion 10

def main():
    H, W = map(int, input().split())
    grid = [list(input()) for _ in range(H)]
    print(H * W - sum([row.count('#') for row in grid]))
