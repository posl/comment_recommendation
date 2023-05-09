def main():
    n,m = map(int,input().split())
    k = [0]*m
    x = [0]*m
    for i in range(m):
        k[i],*x[i] = map(int,input().split())
    for i in range(n):
        for j in range(i+1,n):
            if i+1 not in x and j+1 not in x:
                print('No')
                exit()
    print('Yes')

if __name__ == '__main__':
    main()