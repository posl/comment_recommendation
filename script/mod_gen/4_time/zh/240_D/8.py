def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        b[i] = b[i - 1] + 1
        if a[i] == a[i - 1]:
            b[i] = b[i - 1]
    for i in range(1, n + 1):
        print(b[i])

if __name__ == '__main__':
    main()