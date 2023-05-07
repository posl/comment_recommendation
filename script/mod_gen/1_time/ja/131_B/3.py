def main():
    n, l = map(int, input().split())
    ans = 0
    if l >= 0:
        ans = (l + n - 1) * (l + n) // 2 - l
    elif l + n - 1 < 0:
        ans = (l + n - 1) * (l + n) // 2 - l
    else:
        ans = (l + n - 1) * (l + n) // 2
    print(ans)

if __name__ == '__main__':
    main()