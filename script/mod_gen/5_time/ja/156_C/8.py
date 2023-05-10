def main():
    n = int(input())
    x = list(map(int, input().split()))
    ans = 100000000
    for i in range(1, 101):
        tmp = 0
        for j in range(n):
            tmp += (x[j] - i)**2
        ans = min(ans, tmp)
    print(ans)

if __name__ == '__main__':
    main()