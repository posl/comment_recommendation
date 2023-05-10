Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    H, W, A, B = map(int, input().split())

    print(H, W, A, B)

=======
Suggestion 2

def main():
    H, W, A, B = map(int, input().split())
    print(H, W, A, B)
    print(H, W, A, B)

=======
Suggestion 3

def solve():
    h,w,a,b = map(int,input().split())
    ans = 0
    for i in range(2**h):
        for j in range(2**w):
            cnt = 0
            for k in range(h):
                if i>>k&1:
                    cnt += w
                else:
                    if j>>k&1:
                        cnt += 1
            if cnt == a:
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    h, w, a, b = map(int, input().split())
    ans = 0
    for i in range(h-a):
        for j in range(b, w):
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    H, W, A, B = map(int, input().split())
    print(H, W, A, B)
    print("Hello World")

=======
Suggestion 6

def main():
    H, W, A, B = map(int, input().split())
    print(H, W, A, B)
    print('Hello World!')

=======
Suggestion 7

def calc(h, w, a, b):
    if h == 0 or w == 0:
        return 1
    if (h, w) in memo:
        return memo[(h, w)]
    ret = 0
    if a >= 2 and w >= 2:
        ret += calc(h, w-2, a-2, b)
    if a >= 1 and b >= 1 and w >= 1:
        ret += calc(h-1, w-1, a-1, b-1)
    if b >= 2 and h >= 2:
        ret += calc(h-2, w, a, b-2)
    memo[(h, w)] = ret
    return ret

H, W, A, B = map(int, input().split())
memo = {}
print(calc(H, W, A, B))

=======
Suggestion 8

def dfs(i, j, a, b):
    if i == h:
        return 1
    if j == w:
        return dfs(i+1, 0, a, b)
    if a:
        # 2x1の畳を敷く
        res = dfs(i, j+1, a-1, b)
        # 2x1の畳を縦に敷く
        if i+1 < h and a:
            res += dfs(i, j+1, a-1, b)
    if b:
        # 1x1の畳を敷く
        res += dfs(i, j+1, a, b-1)
    return res

h, w, a, b = map(int, input().split())
print(dfs(0, 0, a, b))

=======
Suggestion 9

def dfs(i, j, a, b):
    if i == h - 1 and j == w:
        return 1
    if j == w:
        j = 0
        i += 1
    if t[i][j]:
        return dfs(i, j + 1, a, b)
    res = 0
    if b:
        t[i][j] = 1
        res += dfs(i, j + 1, a, b - 1)
        t[i][j] = 0
    if a and i < h - 1 and t[i + 1][j] == 0:
        t[i][j] = t[i + 1][j] = 1
        res += dfs(i, j + 1, a - 1, b)
        t[i][j] = t[i + 1][j] = 0
    return res

h, w, a, b = map(int, input().split())
t = [[0] * w for i in range(h)]
print(dfs(0, 0, a, b))
