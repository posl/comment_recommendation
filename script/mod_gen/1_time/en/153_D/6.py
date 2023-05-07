def main():
    h = int(input())
    ans = 0
    while h > 0:
        ans += h
        h >>= 1
    print(ans)

if __name__ == '__main__':
    main()