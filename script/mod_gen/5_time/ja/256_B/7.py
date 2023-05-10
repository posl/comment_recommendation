def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = 0
    for i in range(n):
        p += 1
        p += a[i] - 1
        p %= 4
    print(p)
main()

if __name__ == '__main__':
    main()