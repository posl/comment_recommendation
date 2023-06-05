def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [0] * n
    c = [0] * (2 * 10**5 + 1)
    for i in range(n):
        c[a[i]] += 1
    for i in range(1, 2 * 10**5 + 1):
        c[i] += c[i - 1]
    for i in range(n):
        b[c[a[i]] - 1] = i + 1
        c[a[i]] -= 1
    for i in range(n):
        print(b[i])

if __name__ == '__main__':
    main()