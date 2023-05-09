def main():
    x, y, a, b = map(int, input().split())
    ans = 0
    while a * x < y and a * x < x + b:
        x *= a
        ans += 1
    ans += (y - 1 - x) // b
    print(ans)
main()

if __name__ == '__main__':
    main()