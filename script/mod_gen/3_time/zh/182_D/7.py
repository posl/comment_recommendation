def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    s = 0
    m = 0
    for i in range(n):
        s += a[i]
        if s > m:
            m = s
    print(m)

if __name__ == '__main__':
    main()