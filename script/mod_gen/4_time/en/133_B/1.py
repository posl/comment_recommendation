def main():
    N, D = map(int, input().split())
    X = []
    for i in range(N):
        X.append(list(map(int, input().split())))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            distance = 0
            for k in range(D):
                distance += (X[i][k] - X[j][k])**2
            if int(distance**0.5)**2 == distance:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()