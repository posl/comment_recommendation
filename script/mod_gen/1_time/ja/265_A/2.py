def main():
    x, y, n = map(int, input().split())
    ans = 0
    ans = (n//3) * y + (n%3) * x
    print(ans)

if __name__ == '__main__':
    main()