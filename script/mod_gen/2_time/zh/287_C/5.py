def main():
    n, m = map(int, input().split())
    a = []
    for i in range(m):
        a.append(list(map(int, input().split())))
    a.sort(key=lambda x: x[0])
    for i in range(n - 1):
        if a[i][0] != a[i + 1][0] - 1:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()