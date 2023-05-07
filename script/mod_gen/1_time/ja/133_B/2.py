def main():
    N, D = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            dist = 0
            for d in range(D):
                dist += (X[i][d] - X[j][d]) ** 2
            dist = dist ** 0.5
            if dist.is_integer():
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()