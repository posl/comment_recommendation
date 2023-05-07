def main():
    n, x = map(int, input().split())
    x -= 1
    ans = chr(ord('A') + x % 26)
    if n > 1:
        ans = ans * (n - 1) + chr(ord('A') + x // 26)
    print(ans)

if __name__ == '__main__':
    main()