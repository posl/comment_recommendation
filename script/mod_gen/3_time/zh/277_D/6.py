def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = [0] * m
    for i in a:
        b[i % m] += 1
    ans = 0
    for i in range(m):
        if b[i] == 0:
            continue
        ans += b[i]
        if i == m - i:
            b[i] = 0
        elif b[i] > b[m - i]:
            b[i] = b[m - i]
        else:
            b[m - i] = b[i]
    print(ans)

if __name__ == '__main__':
    main()