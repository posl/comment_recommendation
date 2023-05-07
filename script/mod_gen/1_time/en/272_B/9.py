def main():
    n,m = map(int,input().split())
    a = []
    for i in range(m):
        a.append(list(map(int,input().split())))
    #print(a)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            else:
                #print(i,j)
                flag = 0
                for k in range(m):
                    if i+1 in a[k] and j+1 in a[k]:
                        flag = 1
                        break
                if flag == 0:
                    print('No')
                    return
    print('Yes')

if __name__ == '__main__':
    main()