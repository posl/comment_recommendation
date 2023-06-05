def main():
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(0)
    a.insert(0, 0)
    for i in range(1, n + 1):
        for j in range(i + 1, n + 2):
            if (a[i] - a[j]) ** 2 + (i - j) ** 2 == (a[i] - x) ** 2 + (i - y) ** 2 + (a[j] - x) ** 2 + (j - y) ** 2 and (a[i] - x) * (j - y) == (a[j] - x) * (i - y):
                print("Yes")
                exit()
    print("No")

if __name__ == '__main__':
    main()