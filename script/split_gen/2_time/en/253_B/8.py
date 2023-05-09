def solve(h,w,s):
    for i in range(h):
        for j in range(w):
            if s[i][j] == 'o':
                x1,y1 = i,j
            elif s[i][j] == 'o':
                x2,y2 = i,j
    return max(abs(x1-x2),abs(y1-y2))
h,w = map(int,input().split())
s = [input() for _ in range(h)]
print(solve(h,w,s))
