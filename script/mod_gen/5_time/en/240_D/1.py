def main():
    N = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(2, 2 * 10 ** 5 + 1):
        d[i] = 0
    d[1] = 1
    count = 0
    for i in range(N):
        d[a[i]] += 1
        if d[a[i]] == 2:
            count -= 1
        if d[a[i] + 1] == 0:
            count += 1
        d[a[i] + 1] += 1
        print(count)
    return

if __name__ == '__main__':
    main()