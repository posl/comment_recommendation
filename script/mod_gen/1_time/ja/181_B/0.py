def main():
    n = int(input())
    ans = 0
    for i in range(n):
        a, b = map(int, input().split())
        ans += (b - a + 1) * (a + b) // 2
    print(ans % (10 ** 9 + 7))

if __name__ == '__main__':
    main()