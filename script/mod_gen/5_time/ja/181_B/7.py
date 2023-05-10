def main():
    n = int(input())
    ans = 0
    for _ in range(n):
        a, b = map(int, input().split())
        ans += (b - a + 1) * (a + b) // 2
    print(ans)

if __name__ == '__main__':
    main()