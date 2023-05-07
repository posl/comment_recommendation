def main():
    N = int(input())
    X = [0]*N
    Y = [0]*N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if -1 <= (Y[j]-Y[i])/(X[j]-X[i]) <= 1:
                count += 1
    print(count)

if __name__ == '__main__':
    main()