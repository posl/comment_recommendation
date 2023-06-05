def check(a,b,c,d):
    if a == 1:
        if b == 1:
            return c <= d
        elif b == 2:
            return c < d
        elif b == 3:
            return c < d
        elif b == 4:
            return c < d
    elif a == 2:
        if b == 1:
            return c < d
        elif b == 2:
            return c <= d
        elif b == 3:
            return c < d
        elif b == 4:
            return c < d
    elif a == 3:
        if b == 1:
            return c < d
        elif b == 2:
            return c < d
        elif b == 3:
            return c <= d
        elif b == 4:
            return c < d
    elif a == 4:
        if b == 1:
            return c < d
        elif b == 2:
            return c < d
        elif b == 3:
            return c < d
        elif b == 4:
            return c <= d
n = int(input())
t = []
l = []
r = []
for i in range(n):
    a,b,c = map(int,input().split())
    t.append(a)
    l.append(b)
    r.append(c)
ans = 0
for i in range(n):
    for j in range(i+1,n):
        if check(t[i],t[j],l[i],l[j]) and check(t[i],t[j],l[i],r[j]) and check(t[i],t[j],r[i],l[j]) and check(t[i],t[j],r[i],r[j]):
            ans += 1
print(ans)

if __name__ == '__main__':
    check()