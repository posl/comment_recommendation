def main():
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    max_sum = 0
    for i in range(k):
        max_sum += a[i]
    if max_sum % d == 0:
        print(max_sum)
    else:
        for i in range(k, n):
            if a[i] < d:
                max_sum += a[i]
                if max_sum % d == 0:
                    print(max_sum)
                    exit()
        print(-1)

if __name__ == '__main__':
    main()