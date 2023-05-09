def main():
    n = int(input())
    xyl = [list(map(int, input().split())) for _ in range(n)]
    s = input()
    ans = "No"
    for i in range(n):
        for j in range(i+1, n):
            if s[i] == s[j]:
                continue
            if xyl[i][0] == xyl[j][0] or xyl[i][1] == xyl[j][1]:
                continue
            if (xyl[i][0] < xyl[j][0] and xyl[i][1] < xyl[j][1]) or (xyl[i][0] > xyl[j][0] and xyl[i][1] > xyl[j][1]):
                ans = "Yes"
                break
    print(ans)

if __name__ == '__main__':
    main()