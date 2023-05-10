def main():
    a, n = map(int, input().split())
    if a == 1:
        print(n - 1)
        return
    x = 1
    for i in range(n):
        x *= a
        if x > n:
            print(i)
            return
    print(-1)

if __name__ == '__main__':
    main()