def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = 0
    for i in range(n):
        p += 1
        p -= 1
        p += a[i]
        if p == 4:
            p = 0
    print(p)

if __name__ == '__main__':
    main()