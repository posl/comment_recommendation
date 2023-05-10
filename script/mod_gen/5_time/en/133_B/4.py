def main():
    N,D = map(int,input().split())
    X = []
    for i in range(N):
        x = list(map(int,input().split()))
        X.append(x)
    count = 0
    for i in range(N):
        for j in range(i+1,N):
            sum = 0
            for k in range(D):
                sum += (X[i][k] - X[j][k])**2
            if sum**0.5 == int(sum**0.5):
                count += 1
    print(count)
main()

if __name__ == '__main__':
    main()