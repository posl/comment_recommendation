Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h, w = map(int, input().split())
    c = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if c[i][j] == '.':
                ans += 1
    print(ans)

=======
Suggestion 2

def solve():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if C[i][j] == ".":
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    grid = [list(input()) for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] == ".":
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    C = []
    for _ in range(H):
        C.append(list(input()))

    count = 1
    i = 0
    j = 0
    while True:
        if i == H - 1 and j == W - 1:
            break
        if i < H - 1 and C[i + 1][j] == ".":
            i += 1
            count += 1
            continue
        if j < W - 1 and C[i][j + 1] == ".":
            j += 1
            count += 1
            continue
        break
    print(count)

=======
Suggestion 5

def main():
    h,w = map(int, input().split())
    grid = []
    for _ in range(h):
        grid.append(input())
    dp = [[0 for _ in range(w)] for _ in range(h)]
    dp[0][0] = 1 if grid[0][0] == '.' else 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '.':
                if i-1 >= 0:
                    dp[i][j] += dp[i-1][j]
                if j-1 >= 0:
                    dp[i][j] += dp[i][j-1]
    print(dp[h-1][w-1])

=======
Suggestion 6

def main():
    # Take input Here and Call solution function
    h,w = get_ints_in_variables()
    grid = [get_string() for _ in range(h)]
    # print(grid)
    dp = [[0 for _ in range(w)] for _ in range(h)]
    dp[0][0] = 1 if grid[0][0] == '.' else 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '.':
                if i > 0 and grid[i-1][j] == '.':
                    dp[i][j] = dp[i-1][j]
                if j > 0 and grid[i][j-1] == '.':
                    dp[i][j] += dp[i][j-1]
                dp[i][j] %= mod
    print(dp[h-1][w-1])

=======
Suggestion 7

def main():
    # Take input Here and Call solution function
    H, W = get_ints_in_variables()
    arr = get_list_of_list_in_variable(H)
    # print(H, W, arr)
    print(solution(H, W, arr))

=======
Suggestion 8

def get_input():
    h, w = map(int, input().split())
    grid = []
    for _ in range(h):
        grid.append(input())

    return grid

=======
Suggestion 9

def main():
    H,W = map(int,input().split())
    C = [input() for _ in range(H)]
    print(C)
    print(H,W)
    print(C[0][0])
    print(C[0][1])
    print(C[1][0])
    print(C[1][1])
    print(C[0][W-1])
    print(C[H-1][0])
    print(C[H-1][W-1])
    print(C[0][W-1])
    print(C[H-1][0])
    print(C[H-1][W-1])
    print(C[0][W-1])
    print(C[H-1][0])
    print(C[H-1][W-1])
    print(C[0][W-1])
    print(C[H-1][0])
    print(C[H-1][W-1])
    print(C[0][W-1])
    print(C[H-1][0])
    print(C[H-1][W-1])
    print(C[0][W-1])
    print(C[H-1][0])
    print(C[H-1][W-1])
    print(C[0][W-1])
    print(C[H-1][0])
    print(C[H-1][W-1])
    print(C[0][W-1])
    print(C[H-1][0])
    print(C[H-1][W-1])
    print(C[0][W-1])
    print(C[H-1][0])
    print(C[H-1][W-1])
    print(C[0][W-1])
    print(C[H-1][0])
    print(C[H-1][W-1])

=======
Suggestion 10

def main():
    i = input().split()
    h = int(i[0])
    w = int(i[1])
    a = []
    for j in range(h):
        a.append(input())

    ans = 1
    i = 0
    j = 0
    while True:
        if i == h-1 and j == w-1:
            break
        if i == h-1:
            if a[i][j+1] == ".":
                ans += 1
                j += 1
            else:
                break
        elif j == w-1:
            if a[i+1][j] == ".":
                ans += 1
                i += 1
            else:
                break
        else:
            if a[i][j+1] == "." and a[i+1][j] == ".":
                ans += 1
                if a[i][j+1] == "." and a[i+1][j] == ".":
                    if a[i+1][j+1] == ".":
                        if a[i][j+1] == ".":
                            j += 1
                        else:
                            i += 1
                    else:
                        if a[i][j+1] == ".":
                            j += 1
                        else:
                            i += 1
                else:
                    if a[i][j+1] == ".":
                        j += 1
                    else:
                        i += 1
            else:
                break

    print(ans)
