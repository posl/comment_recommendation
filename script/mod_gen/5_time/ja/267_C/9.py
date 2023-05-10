def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    t = [0] * (n + 1)
    for i in range(n):
        t[i + 1] = s[i + 1] - min(t[i], s[i + 1])
    print(max(t))

if __name__ == '__main__':
    main()