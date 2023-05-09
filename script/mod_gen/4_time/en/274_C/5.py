def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (2 ** n)
    for i in range(n):
        b[a[i]] = i + 1
    c = [0] * (2 ** n)
    for i in range(2 ** n - 1, 0, -1):
        c[i // 2] = max(c[i // 2], c[i] + 1)
    for i in range(1, 2 ** n + 1):
        print(c[b[i]])

if __name__ == '__main__':
    main()