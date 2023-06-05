def main():
    n, x = map(int, input().split())
    x *= 100
    v = 0
    for i in range(n):
        a, b = map(int, input().split())
        v += a * b
        if v > x:
            print(i+1)
            return
    print(-1)

if __name__ == '__main__':
    main()