Synthesizing 10/10 solutions

=======
Suggestion 1

def search(h, w, a, b):
    if h < w:
        h, w = w, h
    if h == 1 and w == 1:
        return 1
    if a == 0:
        return 1
    if a == 1:
        return h - 1
    if a == 2:
        return 1 + (h - 2) * (w - 1)
    if a == 3:
        return 1 + (h - 2) * (w - 1)

=======
Suggestion 2

def solve():
    H, W, A, B = map(int, input().split())
    print(H, W, A, B)
    print(H, W, A, B)

=======
Suggestion 3

def get_input():
    H, W, A, B = map(int, input().split())
    return H, W, A, B

=======
Suggestion 4

def dfs(i, a, b, h, w):
    if i == h*w:
        return 1
    if used[i]:
        return dfs(i+1, a, b, h, w)
    ret = 0
    used[i] = True
    ret += dfs(i+1, a, b, h, w)
    used[i] = False
    if i%w != w-1 and not used[i+1]:
        used[i] = used[i+1] = True
        ret += dfs(i+1, a, b-1, h, w)
        used[i] = used[i+1] = False
    if i+w < h*w and not used[i+w]:
        used[i] = used[i+w] = True
        ret += dfs(i+1, a-1, b, h, w)
        used[i] = used[i+w] = False
    return ret

h, w, a, b = map(int, input().split())
used = [False]*(h*w)
print(dfs(0, a, b, h, w))

=======
Suggestion 5

def solve():
    H,W,A,B = map(int,input().split())
    #print(H,W,A,B)
    ans = 0
    def dfs(i,bit,used):
        if i == H*W:
            nonlocal ans
            ans += 1
            return
        if used>>i&1:
            dfs(i+1,bit,used)
            return
        if i%W != W-1 and not used>>(i+1)&1 and bit>>i&1 == bit>>(i+1)&1:
            dfs(i+1,bit,used|(1<<i)|(1<<(i+1)))
        if i+W < H*W and not used>>(i+W)&1 and bit>>i&1 == bit>>(i+W)&1:
            dfs(i+1,bit,used|(1<<i)|(1<<(i+W)))
        return
    dfs(0,0,(1<<(H*W))-1)
    print(ans)
    return

=======
Suggestion 6

def main():
    H, W, A, B = map(int, input().split())
    print(H, W, A, B)
    print(H*W, A*2+B)

=======
Suggestion 7

def main():
    h, w, a, b = map(int, input().split())
    print(solve(h, w, a, b))

=======
Suggestion 8

def main():
    H, W, A, B = map(int, input().split())
    print(H, W, A, B)

=======
Suggestion 9

def solve(h,w,a,b):
    if h%2==0 and w%2==0:
        return 3
    elif h%2==0 or w%2==0:
        return 2
    else:
        return 1

=======
Suggestion 10

def solve(h,w,a,b):
    if a == 0 and b == 0:
        return 1
    if a == 0:
        return 1
    if b == 0:
        return 1
    if a == 1 and b == 1:
        return 2
    if a == 1:
        return solve(h,w,a,b-1) + solve(h,w,a-1,b)
    if b == 1:
        return solve(h,w,a,b-1) + solve(h,w,a-1,b)
    return solve(h,w,a,b-1) + solve(h,w,a-1,b) + solve(h,w,a-2,b) + solve(h,w,a,b-2)

h,w,a,b = map(int,input().split())
print(solve(h,w,a,b))
