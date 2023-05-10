def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = 0
    for i in range(n):
        if 1 == a[i]:
            p += 1
        elif 2 == a[i]:
            p += 0
        elif 3 == a[i]:
            p += 0
        elif 4 == a[i]:
            p += 1
    print(p)

if __name__ == '__main__':
    main()