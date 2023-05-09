def main():
    h = int(input())
    ans = 0
    while h > 0:
        h >>= 1
        ans += 1
    print(2 ** ans - 1)

if __name__ == '__main__':
    main()