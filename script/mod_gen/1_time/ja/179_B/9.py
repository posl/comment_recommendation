def main():
    n = int(input())
    d = [list(map(int, input().split())) for i in range(n)]
    ans = "No"
    for i in range(n-2):
        if d[i][0] == d[i][1] and d[i+1][0] == d[i+1][1] and d[i+2][0] == d[i+2][1]:
            ans = "Yes"
            break
    print(ans)

if __name__ == '__main__':
    main()