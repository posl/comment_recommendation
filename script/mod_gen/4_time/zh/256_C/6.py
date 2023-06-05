def dfs(i,j,h,w):
    global ans
    if i == 3 and j == 3:
        if h[0] == 0 and h[1] == 0 and h[2] == 0 and w[0] == 0 and w[1] == 0 and w[2] == 0:
            ans += 1
        return
    if i == 3:
        dfs(i,j+1,h,w)
    elif j == 3:
        dfs(i+1,j,h,w)
    else:
        for k in range(1,10):
            if h[i] >= k and w[j] >= k:
                h[i] -= k
                w[j] -= k
                dfs(i,j,h,w)
                h[i] += k
                w[j] += k
    return
ans = 0
h = list(map(int,input().split()))
w = list(map(int,input().split()))
dfs(0,0,h,w)
print(ans)

if __name__ == '__main__':
    dfs()