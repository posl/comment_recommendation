def main():
    n = int(input())
    x = list(map(int, input().split()))
    ans = 10000000000000
    for i in range(1, 101):
        temp = 0
        for j in range(n):
            temp += (x[j] - i) ** 2
        ans = min(ans, temp)
    print(ans)

if __name__ == '__main__':
    main()