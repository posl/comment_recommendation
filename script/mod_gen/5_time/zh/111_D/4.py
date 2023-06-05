def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a,b = map(int,input().split())
        x.append(a)
        y.append(b)
    if n == 1:
        print(0)
        return
    if n == 2:
        if x[0] == x[1] and y[0] == y[1]:
            print(0)
            return
        else:
            print(-1)
            return
    for i in range(n):
        for j in range(i+1,n):
            if x[i] == x[j] and y[i] == y[j]:
                print(-1)
                return
    print(2*n)
    for i in range(n):
        if x[i] < 0:
            print(1,-x[i])
        else:
            print(1,x[i])
        print('R'*abs(x[i]),end='')
        if y[i] < 0:
            print('D'*abs(y[i]),end='')
        else:
            print('U'*abs(y[i]),end='')
        print('L',end='')
        if y[i] < 0:
            print('D'*abs(y[i]),end='')
        else:
            print('U'*abs(y[i]),end='')
        print('R',end='')
        if x[i] < 0:
            print('L'*abs(x[i]),end='')
        else:
            print('R'*abs(x[i]),end='')
        print('U',end='')
        if x[i] < 0:
            print('L'*abs(x[i]),end='')
        else:
            print('R'*abs(x[i]),end='')
        print('D',end='')
        if y[i] < 0:
            print('U'*abs(y[i]),end='')
        else:
            print('D'*abs(y[i]),end='')
        print('L',end='')
        if y[i] < 0:
            print('U'*abs(y[i]),end='')
        else:
            print('D'*abs(y[i]),end='')
        print('R',end='')
        if x[i] < 0:
            print('L'*abs(x[i]),end='')
        else:
            print('R'*abs(x[i]),end='')
        print('U',end='')
        if x[i] < 0:
            print('L'*abs

if __name__ == '__main__':
    main()