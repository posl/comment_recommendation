def main():
    N,S,D = [int(x) for x in input().split()]
    X = []
    Y = []
    for i in range(N):
        x,y = [int(x) for x in input().split()]
        X.append(x)
        Y.append(y)
    for i in range(N):
        if X[i] < S and Y[i] > D:
            print('Yes')
            break
    else:
        print('No')

if __name__ == '__main__':
    main()