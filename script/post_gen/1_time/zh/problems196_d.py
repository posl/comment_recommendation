Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(H, W, A, B):
    if A == 0 and B == 0:
        return 1
    if A == 0:
        return solve(W, H, B, A)
    if H == 1:
        return 1
    res = 0
    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                continue
            if i == 0 and j == 1:
                continue
            if i == 1 and j == 0:
                continue
            if i == 1 and j == 1:
                continue
            res += solve(i, j, A-1, B) * solve(H-i, j, 0, B) + solve(i, W-j, A-1, B) * solve(H-i, W-j, 0, B) + solve(i, j, A-1, B) * solve(H-i, W-j, 0, B) + solve(i, W-j, A-1, B) * solve(H-i, j, 0, B)
    return res

H, W, A, B = map(int, input().split())
print(solve(H, W, A, B))

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def main():
    H, W, A, B = map(int, input().split())
    print(rec(0, 0, A, B, H, W))

=======
Suggestion 4

def dfs(h, w, a, b):
    if h < 0 or w < 0:
        return 0
    if h == 0 and w == 0:
        return 1
    if (h, w, a, b) in memo:
        return memo[(h, w, a, b)]
    res = 0
    if a:
        res += dfs(h-1, w, a-1, b) + dfs(h-2, w, a-1, b)
    if b:
        res += dfs(h, w-1, a, b-1) + dfs(h, w-2, a, b-1)
    memo[(h, w, a, b)] = res
    return res

H, W, A, B = map(int, input().split())
memo = {}
print(dfs(H, W, A, B))

=======
Suggestion 5

def solve(h, w, a, b):
    if a < 0 or b < 0:
        return 0
    if h == 0 and w == 0:
        return 1
    if h < 0 or w < 0:
        return 0
    if h < 2 and w < 2:
        return 0
    if h < 2:
        return solve(w, h, b, a)
    if w < 2:
        return solve(h, w, a, b)
    if h > w:
        return solve(h-2, w, a-1, b) + solve(h, w-2, a-1, b) + solve(h-1, w-1, a, b-1)
    return solve(h-2, w, a-1, b) + solve(h, w-2, a-1, b) + solve(h-1, w-1, a, b-1) + solve(h-1, w-1, a-1, b)

=======
Suggestion 6

def solve(H,W,A,B):
    if A==0 and B==0:
        return 1
    if A==0:
        return solve(W,H,B,A)
    if H==1:
        return solve(W,1,B-1,0)
    if W==1:
        return solve(1,H,B-1,0)
    return solve(H-1,W,A-1,B)+solve(H,W-1,A-1,B)

H,W,A,B=map(int,input().split())
print(solve(H,W,A,B))

=======
Suggestion 7

def main():
    h,w,a,b = map(int,input().split())
    print(h*w-2*a-b)

=======
Suggestion 8

def main():
    H, W, A, B = map(int, input().split())
    print(H, W, A, B)
    print(f(H, W, A, B))

=======
Suggestion 9

def f(h,w,a,b):
    if h==0 and w==0:
        return 1
    if h<0 or w<0:
        return 0
    if h<w:
        h,w=w,h
    if h==w:
        return f(h-1,w-1,a,b)
    return f(h-1,w,a,b)+f(h-2,w,a,b)+f(h-1,w-1,a,b)+f(h-2,w-2,a,b)

h,w,a,b=map(int,input().split())
print(f(h,w,a,b))

=======
Suggestion 10

def f(h,w,a,b):
    if h == 1 and w == 1:
        return 1
    if h == 1:
        return f(1,w-1,b,a)
    if w == 1:
        return f(h-1,1,a,b)
    if h == 2 and w == 2:
        return 4
    if h == 2:
        return f(2,w-1,b,a) + f(2,w-2,b,a)
    if w == 2:
        return f(h-1,2,a,b) + f(h-2,2,a,b)
    return f(h-1,w,a,b) + f(h-2,w,a,b) + f(h,w-1,a,b) + f(h,w-2,a,b)

h,w,a,b = map(int,input().split())
print(f(h,w,a,b))
