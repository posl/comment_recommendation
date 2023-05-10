def main():
    x = input()
    m = int(input())
    d = int(max(x))
    ans = 0
    while True:
        try:
            ans += int(x, d+1) <= m
            d += 1
        except ValueError:
            break
    print(ans)
main()

if __name__ == '__main__':
    main()