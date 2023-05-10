def main():
    n,m,t = map(int,input().split())
    a = []
    b = []
    for i in range(m):
        ai,bi = map(int,input().split())
        a.append(ai)
        b.append(bi)
    battery = n
    flag = True
    for i in range(m):
        if i == 0:
            battery = battery - (a[i] - 0.5)
        else:
            battery = battery - (a[i] - b[i-1] - 1)
        if battery <= 0:
            flag = False
            break
        battery = battery + (b[i] - a[i] + 1)
        if battery >= n:
            battery = n
    battery = battery - (t - b[m-1] - 0.5)
    if battery <= 0:
        flag = False
    if flag:
        print("Yes")
    else:
        print("No")
