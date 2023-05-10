def bfs(h,w):
    global n, m
    if n==1:
        if m==1:
            return 0
        else:
            return -1
    if h==0 and w==0:
        return 0
    if h==0:
        if w%2==1:
            return 2
        else:
            return 1
    if w==0:
        if h%2==1:
            return 2
        else:
            return 1
    if h%2==0 and w%2==0:
        return 2
    else:
        return 1
n, m = map(int, input().split())
for i in range(n):
    for j in range(n):
        print(bfs(i,j), end=" ")
    print()

if __name__ == '__main__':
    bfs()