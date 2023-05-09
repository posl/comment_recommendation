def main():
    n,s,d = map(int,input().split())
    x = []
    y = []
    for i in range(n):
        x_i,y_i = map(int,input().split())
        x.append(x_i)
        y.append(y_i)
    for i in range(n):
        if x[i] < s and y[i] > d:
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    main()