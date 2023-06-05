def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        tmp = input().split()
        x.append(int(tmp[0]))
        y.append(int(tmp[1]))
    if n==1:
        print(0)
        print('')
        print('')
    elif n==2:
        if x[0]==x[1] or y[0]==y[1]:
            print(1)
            print(1)
            if x[0]<x[1]:
                print('R')
            elif x[0]>x[1]:
                print('L')
            elif y[0]<y[1]:
                print('U')
            elif y[0]>y[1]:
                print('D')
        else:
            print(-1)
    elif n==3:
        if x[0]==x[1]==x[2] or y[0]==y[1]==y[2]:
            print(2)
            print(1,1)
            if x[0]<x[1]:
                print('R')
            elif x[0]>x[1]:
                print('L')
            elif y[0]<y[1]:
                print('U')
            elif y[0]>y[1]:
                print('D')
            for i in range(1,3):
                if x[i]<x[(i+1)%3]:
                    print('R')
                elif x[i]>x[(i+1)%3]:
                    print('L')
                elif y[i]<y[(i+1)%3]:
                    print('U')
                elif y[i]>y[(i+1)%3]:
                    print('D')
        else:
            print(-1)
    else:
        print(-1)

if __name__ == '__main__':
    main()