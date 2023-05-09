def main():
    n = int(input())
    xyp = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            xi, yi, pi = xyp[i]
            xj, yj, pj = xyp[j]
            if pi * ans >= abs(xi - xj) + abs(yi - yj):
                ans += 1
                break
    print(ans)

if __name__ == '__main__':
    main()