def main():
    n = int(input())
    ans = n // 100
    if n % 100 != 0:
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()