def main():
    n, d = map(int, input().split())
    x = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            sum = 0
            for k in range(d):
                sum += (x[i][k] - x[j][k]) ** 2
            if sum ** 0.5 % 1 == 0:
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()