def main():
    #输入
    n, m, x, y = map(int, input().split())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    #处理
    X.sort()
    Y.sort()
    #print(X)
    #print(Y)
    Z = [i for i in range(x+1, y+1)]
    #print(Z)
    if len(Z) == 0:
        print("战争")
    else:
        for i in Z:
            if i > X[-1] and i <= Y[0]:
                print("合法")
                break
        else:
            print("战争")

if __name__ == '__main__':
    main()