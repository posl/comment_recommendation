def main():
    N,D = map(int,input().split())
    X = []
    Y = []
    for i in range(N):
        x,y = map(int,input().split())
        X.append(x)
        Y.append(y)
    count = 0
    for i in range(N):
        if ((X[i]**2+Y[i]**2)**(1/2)) <= D:
            count += 1
    print(count)
