def main():
    N, D = map(int, input().split())
    X = []
    for i in range(N):
        X.append(list(map(int, input().split())))
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            dist = 0
            for k in range(D):
                dist += (X[i][k] - X[j][k]) ** 2
            if dist ** 0.5 == int(dist ** 0.5):
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()