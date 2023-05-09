def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    m = a[0] - 1
    for i in range(1, len(a)):
        m -= a[i]
    print(m)

if __name__ == '__main__':
    main()