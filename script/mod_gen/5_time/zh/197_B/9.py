def check(a,b):
    if a < 0 or b < 0 or a >= h or b >= w:
        return False
    if s[a][b] == "#":
        return False
    return True
h,w,x,y = map(int,input().split())
s = [input() for _ in range(h)]
ans = 1
for i in range(1,x):
    if not check(x-i-1,y-1):
        break
    ans += 1
for i in range(x,h):
    if not check(i,y-1):
        break
    ans += 1
for i in range(1,y):
    if not check(x-1,y-i-1):
        break
    ans += 1
for i in range(y,w):
    if not check(x-1,i):
        break
    ans += 1
print(ans)

if __name__ == '__main__':
    check()