def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    x -= 1
    count = 0
    check = [0 for i in range(n)]
    while True:
        if check[x] == 0:
            check[x] = 1
            count += 1
            x = a[x] - 1
        else:
            break
    print(count)
main()

if __name__ == '__main__':
    main()