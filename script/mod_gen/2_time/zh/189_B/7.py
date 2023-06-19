def main():
    n, x = map(int, input().split())
    sum = 0
    for i in range(n):
        v, p = map(int, input().split())
        sum += v * p
        if sum > x * 100:
            print(i + 1)
            exit()
    print(-1)

if __name__ == '__main__':
    main()