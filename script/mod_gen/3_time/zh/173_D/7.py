def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.append(a[0])
    s = sum(a)
    m = 0
    for i in range(n):
        s -= a[i]
        m = max(m, a[i] + s)
    print(m)

if __name__ == '__main__':
    main()