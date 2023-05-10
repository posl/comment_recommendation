def main():
    d, n = map(int, input().split())
    ans = (100 ** d) * n
    if n == 100:
        ans += 100 ** d
    print(ans)

if __name__ == '__main__':
    main()