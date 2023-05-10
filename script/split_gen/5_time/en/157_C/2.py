def main():
    n,m = map(int,input().split())
    s = []
    c = []
    for i in range(m):
        s1,c1 = map(int,input().split())
        s.append(s1)
        c.append(c1)
    if n == 1:
        for i in range(10):
            if i == c[0]:
                print(i)
                return
        print(-1)
        return
    if n == 2:
        for i in range(10):
            for j in range(10):
                if i == c[0] and j == c[1]:
                    print(str(i)+str(j))
                    return
        print(-1)
        return
    if n == 3:
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    if i == c[0] and j == c[1] and k == c[2]:
                        print(str(i)+str(j)+str(k))
                        return
        print(-1)
        return
