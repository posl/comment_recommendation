def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x,y = map(int,input().split())
        X.append(x)
        Y.append(y)
    count = 0
    for i in range(0,N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                x1 = X[i]
                y1 = Y[i]
                x2 = X[j]
                y2 = Y[j]
                x3 = X[k]
                y3 = Y[k]
                if (x1-x2)*(y1-y3) != (x1-x3)*(y1-y2):
                    count += 1
    print(count)
