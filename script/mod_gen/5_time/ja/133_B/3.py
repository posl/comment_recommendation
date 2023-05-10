def main():
    n, d = map(int, input().split())
    x = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            dis = 0
            for k in range(d):
                dis += (x[i][k] - x[j][k]) ** 2
            if (dis ** 0.5).is_integer():
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()