def main():
    n, m = map(int, input().split())
    a = [0] * (n + 1)
    for i in range(m):
        a[int(input())] = 1
    b = [0] * (n + 1)
    b[0] = 1
    for i in range(1, n + 1):
        if a[i] == 1:
            continue
        b[i] = (b[i - 1] + b[i - 2]) % 1000000007
    print(b[n])

if __name__ == '__main__':
    main()