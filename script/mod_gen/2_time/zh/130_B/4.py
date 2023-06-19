def main():
    n,x = map(int, input().split())
    l = list(map(int, input().split()))
    d = 0
    count = 1
    for i in range(n):
        if d <= x:
            d += l[i]
            count += 1
    print(count)

if __name__ == '__main__':
    main()