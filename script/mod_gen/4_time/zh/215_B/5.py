def main():
    n = int(input())
    ans = 0
    while n >= 2:
        n = n // 2
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()