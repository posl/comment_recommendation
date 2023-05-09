def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    i = 0
    j = 0
    min = 1000000001
    while i < n and j < m:
        if a[i] <= b[j]:
            if min > b[j] - a[i]:
                min = b[j] - a[i]
            i += 1
        else:
            if min > a[i] - b[j]:
                min = a[i] - b[j]
            j += 1
    print(min)

if __name__ == '__main__':
    main()