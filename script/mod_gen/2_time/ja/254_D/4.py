def main():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i * j <= n:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()