def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = 0
    for i in range(n):
        if i == 0:
            p = 0
        else:
            p += a[i-1]
        if p > 3:
            p = 3
    print(p)

if __name__ == '__main__':
    main()