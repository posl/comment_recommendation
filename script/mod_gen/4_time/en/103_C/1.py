def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    m = a[0]
    for i in range(1, n):
        m = min(m, a[i] - a[i - 1])
    print(m)

if __name__ == '__main__':
    main()