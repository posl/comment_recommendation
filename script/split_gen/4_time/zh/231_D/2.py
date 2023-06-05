def check(n,m,ai,bi):
    #print(n,m,ai,bi)
    if n == 1:
        print("Yes")
        return
    if m == 0:
        print("No")
        return
    if m == 1:
        print("Yes")
        return
    if m == 2:
        if ai[0] == 1 or ai[1] == 1 or bi[0] == n or bi[1] == n:
            print("Yes")
        else:
            print("No")
        return
    if m == 3:
        if ai[0] == 1 or ai[1] == 1 or ai[2] == 1 or bi[0] == n or bi[1] == n or bi[2] == n:
            print("Yes")
        else:
            print("No")
        return
    print("Yes")
    return
n,m = map(int,input().split())
ai = []
bi = []
for i in range(m):
    a,b = map(int,input().split())
    ai.append(a)
    bi.append(b)
check(n,m,ai,bi)
