def check(x,y):
    if x < 0 or x >= h or y < 0 or y >= w:
        return False
    if s[x][y] == '#':
        return False
    return True
h,w,x,y = map(int,input().split())
s = [input() for _ in range(h)]
ans = 1
x -= 1
y -= 1
for i in range(1,h):
    if check(x-i,y):
        ans += 1
    else:
        break
for i in range(1,w):
    if check(x,y-i):
        ans += 1
    else:
        break
for i in range(1,h):
    if check(x+i,y):
        ans += 1
    else:
        break
for i in range(1,w):
    if check(x,y+i):
        ans += 1
    else:
        break
print(ans)

if __name__ == '__main__':
    check()