def main():
    N = int(input())
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        x, y = map(int, input().split())
        X[i] = x
        Y[i] = y
    
    ans = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if -1 <= (Y[j]-Y[i])/(X[j]-X[i]) <= 1:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()