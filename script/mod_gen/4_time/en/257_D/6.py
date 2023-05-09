def main():
    n = int(input())
    xyp = []
    for _ in range(n):
        xyp.append(list(map(int, input().split())))
    ans = 1
    for i in range(n):
        for j in range(i+1, n):
            if xyp[i][2] * ans >= abs(xyp[i][0] - xyp[j][0]) + abs(xyp[i][1] - xyp[j][1]):
                ans += 1
                break
    print(ans)

if __name__ == '__main__':
    main()