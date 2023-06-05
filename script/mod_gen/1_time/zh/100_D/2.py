def main():
    N,M = map(int,input().split())
    X = []
    Y = []
    Z = []
    for i in range(N):
        x,y,z = map(int,input().split())
        X.append(x)
        Y.append(y)
        Z.append(z)
    max = 0
    for i in range(2**3):
        x = 1
        y = 1
        z = 1
        for j in range(3):
            if i & 1<<j:
                x *= -1
            if i & 1<<(j+1):
                y *= -1
            if i & 1<<(j+2):
                z *= -1
        X.sort(reverse=True)
        Y.sort(reverse=True)
        Z.sort(reverse=True)
        s = 0
        for j in range(M):
            s += (X[j]*x + Y[j]*y + Z[j]*z)
        if max < s:
            max = s
    print(max)

if __name__ == '__main__':
    main()