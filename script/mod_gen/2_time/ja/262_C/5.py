def main():
    n = int(input())
    a = list(map(int, input().split()))
    l = [0] * (n + 1)
    for i, v in enumerate(a):
        l[v] = i + 1
    r = 0
    m = n + 1
    for i in range(n, 0, -1):
        if l[i] < m:
            r += 1
        m = min(m, l[i])
    print(r)

if __name__ == '__main__':
    main()