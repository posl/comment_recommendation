def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    if a[0] > 0:
        print(0)
        return
    for i in range(1, n):
        if a[i] - a[i - 1] > 1:
            print(a[i - 1] + 1)
            return
    print(a[-1] + 1)

if __name__ == '__main__':
    main()