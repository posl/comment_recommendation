def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a,b = map(int,input().split())
        x.append(a)
        y.append(b)
    #print(x)
    #print(y)
    if n == 1:
        print(0)
        print(1)
        print("U")
        return
    if n == 2:
        if x[0] == x[1] and y[0] == y[1]:
            print(0)
            print(1)
            print("U")
            return
        else:
            print(-1)
            return
    if n == 3:
        if x[0] == x[1] and x[1] == x[2]:
            if y[0] < y[1] and y[1] < y[2]:
                print(2)
                print(1,1)
                print("UD")
                print("UD")
                print("UD")
                return
            elif y[0] > y[1] and y[1] > y[2]:
                print(2)
                print(1,1)
                print("DU")
                print("DU")
                print("DU")
                return
            else:
                print(-1)
                return
        elif y[0] == y[1] and y[1] == y[2]:
            if x[0] < x[1] and x[1] < x[2]:
                print(2)
                print(1,1)
                print("RL")
                print("RL")
                print("RL")
                return
            elif x[0] > x[1] and x[1] > x[2]:
                print(2)
                print(1,1)
                print("LR")
                print("LR")
                print("LR")
                return
            else:
                print(-1)
                return
        else:
            print(-1)
            return
    if n == 4:
        if x[0] == x[1] and x[1] == x[2] and x[2] == x[3]:
            if y[0] < y[1] and y[1] < y[2] and y[2] < y[3]:
                print(2)
                print(1,

if __name__ == '__main__':
    main()