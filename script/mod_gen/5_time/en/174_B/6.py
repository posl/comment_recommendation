def main():
    n, d = map(int, input().split())
    ans = 0
    for _ in range(n):
        x, y = map(int, input().split())
        if (x*x + y*y) <= d*d:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()