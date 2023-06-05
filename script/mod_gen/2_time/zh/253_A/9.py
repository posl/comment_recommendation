def main():
    n = int(input())
    a = list(map(int, input().split()))
    c = [0] * 200005
    for i in range(n):
        c[a[i]] += 1
    s = 0
    for i in range(200005):
        s += c[i] * (c[i] - 1) * (c[i] - 2) // 6
    for i in range(200005):
        s -= c[i] * (c[i] - 1) // 2 * (n - c[i])
    for i in range(200005):
        for j in range(i + 1, 200005):
            s -= c[i] * c[j] * (c[j] - 1) // 2
    print(s)

if __name__ == '__main__':
    main()