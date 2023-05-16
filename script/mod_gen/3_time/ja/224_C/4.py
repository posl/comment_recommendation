def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x,y = map(int,input().split())
        X.append(x)
        Y.append(y)
    count = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if (X[i]-X[k])*(Y[j]-Y[k]) != (X[j]-X[k])*(Y[i]-Y[k]):
                    count += 1
    print(count)
main()

if __name__ == '__main__':
    main()