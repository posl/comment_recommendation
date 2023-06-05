def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = 0
    for i in range(n):
        p += 1
        if a[i] == 1:
            p += 1
        elif a[i] == 2:
            p += 2
        elif a[i] == 3:
            p += 3
        else:
            p += 4
    print(p)

if __name__ == '__main__':
    main()