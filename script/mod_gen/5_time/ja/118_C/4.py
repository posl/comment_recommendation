def main():
    n = int(input())
    a = list(map(int, input().split()))
    while len(a) > 1:
        a.sort()
        a[0] = a[0] % a[1]
        if a[0] == 0:
            a.pop(0)
    print(a[0])

if __name__ == '__main__':
    main()