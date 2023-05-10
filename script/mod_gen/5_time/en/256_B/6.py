def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    p = 0
    for i in range(n):
        if a[i] == 1:
            p += 1
        elif a[i] == 2:
            p += 0
        elif a[i] == 3:
            p += 1
        elif a[i] == 4:
            p += 0
    print(p)

if __name__ == '__main__':
    main()