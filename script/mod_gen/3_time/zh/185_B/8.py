def main():
    n,m,t = map(int,input().split())
    a = []
    b = []
    for i in range(m):
        x,y = map(int,input().split())
        a.append(x)
        b.append(y)
    for i in range(m):
        if i == 0:
            if a[i] != 1:
                print("No")
                return
        else:
            if a[i] - b[i-1] > 1:
                print("No")
                return
    if t - b[m-1] > 1:
        print("No")
        return
    print("Yes")
    return
main()
