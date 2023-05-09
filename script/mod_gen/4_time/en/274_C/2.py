def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (2 ** (n + 1))
    for i in range(n):
        b[a[i]] = i + 1
    for i in range(1, 2 ** (n + 1)):
        if b[i] == 0:
            b[i] = b[i // 2]
    for i in range(1, 2 ** (n + 1)):
        print(b[i] - 1)

if __name__ == '__main__':
    main()