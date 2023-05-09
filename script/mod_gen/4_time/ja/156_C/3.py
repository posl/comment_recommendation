def main():
    n = int(input())
    x = list(map(int, input().split()))
    ans = 0
    for i in range(101):
        tmp = 0
        for j in range(n):
            tmp += (x[j] - i) ** 2
        if i == 0:
            ans = tmp
        else:
            ans = min(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()