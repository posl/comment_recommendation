def main():
    n,m,t = map(int,input().split())
    a = list(map(int,input().split()))
    xy = []
    for i in range(m):
        xy.append(list(map(int,input().split())))
    for i in range(1,n):
        if a[i-1] >= a[i]:
            print("No")
            return
    for i in range(m):
        if a[xy[i][0]-2] >= a[xy[i][0]-1] - xy[i][1]:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()