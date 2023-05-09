def main():
    n,m = map(int, input().split())
    kx = []
    for i in range(m):
        kx.append(list(map(int, input().split())))
    #print(n,m)
    #print(kx)
    flag = False
    for i in range(m):
        for j in range(i+1, m):
            #print("i,j", i,j)
            #print(kx[i])
            #print(kx[j])
            #print(set(kx[i][1:]) & set(kx[j][1:]))
            if len(set(kx[i][1:]) & set(kx[j][1:])) > 0:
                flag = True
                break
        if flag:
            break
    if flag:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()