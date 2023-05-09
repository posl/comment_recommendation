def main():
    N = int(input())
    X = [0]*N
    Y = [0]*N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans += ((X[i]-X[j])**2+(Y[i]-Y[j])**2)**0.5
    print(ans*N*2/N/N)

if __name__ == '__main__':
    main()