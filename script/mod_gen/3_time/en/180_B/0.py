def main():
    n = int(input())
    x = list(map(int, input().split()))
    m = 0
    e = 0
    c = 0
    for i in range(n):
        m += abs(x[i])
        e += x[i] ** 2
        if abs(x[i]) > c:
            c = abs(x[i])
    e = e ** 0.5
    print(m)
    print(e)
    print(c)

if __name__ == '__main__':
    main()