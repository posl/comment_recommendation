def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = 0
    for i in range(n):
        if i == 0:
            p += 1
        else:
            if a[i-1] == 1:
                p += 1
            elif a[i-1] == 2:
                p += 1
            elif a[i-1] == 3:
                p += 2
            elif a[i-1] == 4:
                p += 3
    print(p)

if __name__ == '__main__':
    main()