def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [0] + a
    b = [0] * (2 ** (n + 1))
    for i in range(1, 2 ** n + 1):
        b[i] = a[i]
    for i in range(n):
        for j in range(1, 2 ** (n - i) + 1):
            b[j] = max(b[2 * j], b[2 * j - 1])
    for i in range(2 ** n + 1, 2 ** (n + 1)):
        if a[i] == b[1]:
            print(i - (2 ** n))
            exit()

if __name__ == '__main__':
    main()