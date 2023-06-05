def main():
    n = int(input().strip())
    ans = 0
    for i in range(1, n):
        ans += (n - 1) // i
    print(ans)

if __name__ == '__main__':
    main()