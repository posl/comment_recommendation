def main():
    n,m = map(int, input().split())
    #print(n,m)
    #print(type(n),type(m))
    a = []
    b = []
    for i in range(m):
        ai,bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    #print(a)
    #print(b)
    #各个岛屿的连接数
    c = [0 for i in range(n)]
    for i in range(m):
        c[a[i]-1] += 1
        c[b[i]-1] += 1
    #print(c)
    #计算桥梁数
    bridge = 0
    for i in range(n):
        bridge += c[i]//2
    #print(bridge)
    #计算拆除桥梁数
    #拆除桥梁的条件：必须是两个岛屿之间的桥梁，且岛屿的连接数都大于2
    remove = 0
    for i in range(m):
        if c[a[i]-1] > 2 and c[b[i]-1] > 2:
            remove += 1
    #print(remove)
    #print(bridge - remove)
    print(bridge - remove)
