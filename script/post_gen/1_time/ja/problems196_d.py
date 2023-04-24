Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W, A, B = map(int, input().split())
    print(H, W, A, B)

=======
Suggestion 2

def main():
    h, w, a, b = map(int, input().split())
    print(solve(h, w, a, b))

=======
Suggestion 3

def f(h, w, a, b):
    if h < 2 or w < 2:
        return 1
    if a == 0:
        return f(h - 1, w, a, b) + f(h, w - 1, a, b)
    return f(h - 1, w, a, b) + f(h, w - 1, a, b) + f(h - 2, w, a - 1, b) + f(h, w - 2, a - 1, b)

h, w, a, b = map(int, input().split())
print(f(h, w, a, b))

=======
Suggestion 4

def main():
    H, W, A, B = map(int, input().split())
    ans = 0
    dp = [[0 for _ in range(W)] for _ in range(H)]
    def dfs(i, j, a, b):
        if a < 0 or b < 0:
            return 0
        if j == W:
            j = 0
            i += 1
        if i == H:
            return 1
        if dp[i][j] != 0:
            return dp[i][j]
        res = 0
        #畳を置かない場合
        res += dfs(i, j + 1, a, b)
        if (a > 0):
            #2x1畳を置く場合
            if (j + 1 < W) and (dp[i][j + 1] == 0):
                dp[i][j + 1] = 1
                res += dfs(i, j + 1, a - 1, b)
                dp[i][j + 1] = 0
            #2x2畳を置く場合
            if (i + 1 < H) and (dp[i + 1][j] == 0):
                dp[i + 1][j] = 1
                res += dfs(i, j + 1, a - 1, b - 1)
                dp[i + 1][j] = 0
        if (b > 0):
            #1x1畳を置く場合
            if (dp[i][j] == 0):
                dp[i][j] = 1
                res += dfs(i, j + 1, a, b - 1)
                dp[i][j] = 0
        dp[i][j] = res
        return res
    ans = dfs(0, 0, A, B)
    print(ans)

=======
Suggestion 5

def main():
    H, W, A, B = map(int, input().split())
    ans = 0
    for i in range(1 << (H*W)):
        bit = i
        a = 0
        b = 0
        for j in range(H):
            for k in range(W):
                if bit & 1:
                    a += 1
                else:
                    b += 1
                bit >>= 1
            bit >>= W
        if a == A and b == B:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    H, W, A, B = map(int, input().split())
    print(H, W, A, B)
    print("Hello World!")
    return

=======
Suggestion 7

def calc_combination(n, r):
    return calc_factorial(n) // (calc_factorial(n - r) * calc_factorial(r))

=======
Suggestion 8

def get_tile_num(H, W, A, B):
    if H == 1 and W == 1:
        return 1
    if W == 1:
        return get_tile_num(H-1, W, B, A)
    if A == 0:
        return 1
    if H == 1:
        return get_tile_num(H, W-1, A-1, B)
    return get_tile_num(H-1, W, B, A) + get_tile_num(H, W-1, A-1, B)

=======
Suggestion 9

def getPattern(H, W, A, B):
    #print("getPattern({},{},{},{})".format(H, W, A, B))
    if H == 0 and W == 0:
        return 1
    if H == 0:
        return getPattern(H, W-1, A, B) + getPattern(H, W-1, A-1, B)
    if W == 0:
        return getPattern(H-1, W, A, B) + getPattern(H-1, W, A, B-1)
    return getPattern(H, W-1, A, B) + getPattern(H-1, W, A, B)

=======
Suggestion 10

def main():
    h,w,a,b = map(int,input().split())
    print(h,w,a,b)
    print('----------------------')
    print(h*w,a+b)
    print('----------------------')
    print(h*w/(a+b))
    print('----------------------')
    print(h*w//(a+b))
    print('----------------------')

    #縦横を入れ替えた場合の数を求める
    h,w = w,h
    print(h,w,a,b)
    print('----------------------')
    print(h*w,a+b)
    print('----------------------')
    print(h*w/(a+b))
    print('----------------------')
    print(h*w//(a+b))
    print('----------------------')

    print((h*w//(a+b)) * (h*w//(a+b)))
