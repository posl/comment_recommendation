def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        if a[i] not in d:
            d[a[i]] = 1
        else:
            d[a[i]] += 1
    print(sum([d[i] * (d[i] - 1) // 2 for i in d]))

if __name__ == '__main__':
    main()