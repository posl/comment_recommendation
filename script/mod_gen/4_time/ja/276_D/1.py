def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    while 1:
        for i in range(n):
            if a[i] % 2 == 0:
                a[i] = a[i] / 2
            elif a[i] % 3 == 0:
                a[i] = a[i] / 3
            else:
                count = -1
                break
        if count == -1:
            break
        else:
            count += 1
        if a.count(a[0]) == n:
            break
    print(count)

if __name__ == '__main__':
    main()