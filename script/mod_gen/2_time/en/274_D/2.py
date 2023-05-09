def main():
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(0)
    a.insert(0, 0)
    for i in range(1, n + 2):
        for j in range(i + 1, n + 2):
            if abs(i - j) == 1:
                continue
            if abs(a[i] - a[j]) == abs(i - j):
                print('No')
                return
    print('Yes')

if __name__ == '__main__':
    main()