def main():
    n = int(input())
    x = [int(i) for i in input().split()]
    x = sorted(x)
    ans = 0
    for i in range(n):
        ans += (x[i] - x[n // 2]) ** 2
    print(ans)

if __name__ == '__main__':
    main()