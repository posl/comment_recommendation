def move(p, a):
    #print("move", p, a)
    p += 1
    #print("p:", p)
    if p == 4:
        p = 0
    p += a
    #print("p:", p)
    if p >= 4:
        p -= 4
    return p
n = int(input())
a = list(map(int, input().split()))
p = 0
ans = 0
for i in range(n):
    #print("i:", i)
    #print("a[i]:", a[i])
    if p == 0:
        ans += 1
    p = move(p, a[i])
print(ans)

if __name__ == '__main__':
    move()