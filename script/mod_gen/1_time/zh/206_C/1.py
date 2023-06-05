def main():
    n = int(input())
    if n < 2 or n > 3 * 10 ** 5:
        return
    a = list(map(int, input().split()))
    if len(a) != n:
        return
    # print(a)
    count = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if a[i] != a[j]:
                count += 1
    print(count)

if __name__ == '__main__':
    main()