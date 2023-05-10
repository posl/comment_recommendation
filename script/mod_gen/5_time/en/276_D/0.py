def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n):
        while a[i] % 2 == 0:
            a[i] = a[i] / 2
            count += 1
        while a[i] % 3 == 0:
            a[i] = a[i] / 3
            count += 1
    if len(set(a)) == 1:
        print(count)
    else:
        print(-1)

if __name__ == '__main__':
    main()