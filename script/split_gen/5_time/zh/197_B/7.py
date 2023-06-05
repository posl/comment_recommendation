def main():
    h,w,x,y = map(int,input().split())
    s = []
    for i in range(h):
        s.append(input())
    x -= 1
    y -= 1
    ans = 0
    for i in range(x,-1,-1):
        if s[i][y] == '#':
            break
        ans += 1
    for i in range(x,h):
        if s[i][y] == '#':
            break
        ans += 1
    for i in range(y,-1,-1):
        if s[x][i] == '#':
            break
        ans += 1
    for i in range(y,w):
        if s[x][i] == '#':
            break
        ans += 1
    print(ans-3)
