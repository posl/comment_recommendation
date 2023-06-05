def main():
    x = int(input())
    ans = 0
    ans += (x // 500) * 1000
    x %= 500
    ans += (x // 5) * 5
    print(ans)

if __name__ == '__main__':
    main()