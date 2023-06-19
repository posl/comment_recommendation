def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a[x-1] = 0
    c = 1
    for i in range(n):
        if a[i] == 0:
            continue
        else:
            c += 1
            a[a[i]-1] = 0
    print(c)

if __name__ == '__main__':
    main()