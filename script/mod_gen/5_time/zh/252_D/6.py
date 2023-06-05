def main():
    n = int(input())
    a = list(map(int, input().split()))
    #print(a)
    #print(n)
    b = [0 for i in range(200001)]
    #print(b)
    for i in range(n):
        b[a[i]] += 1
    #print(b)
    c = [0 for i in range(200001)]
    #print(c)
    for i in range(200000):
        c[i + 1] = c[i] + b[i]
    #print(c)
    ans = 0
    for i in range(200000):
        if b[i] > 1:
            ans += b[i] * (b[i] - 1) // 2 * (c[i] - b[i])
        if b[i] > 2:
            ans += b[i] * (b[i] - 1) * (b[i] - 2) // 6
    print(ans)

if __name__ == '__main__':
    main()