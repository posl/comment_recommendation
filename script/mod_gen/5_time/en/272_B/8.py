def main():
    n,m = map(int,input().split())
    x = []
    for i in range(m):
        x.append(list(map(int,input().split())))
    for i in range(1,n+1):
        if x[0][0] in x[i-1][1:]:
            if x[i-1][0] in x[0][1:]:
                print('Yes')
                exit()
    print('No')

if __name__ == '__main__':
    main()