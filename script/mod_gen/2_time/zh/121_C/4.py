def main():
    n, m = map(int, input().split())
    arr = []
    for i in range(n):
        a, b = map(int, input().split())
        arr.append((a, b))
    arr.sort(key=lambda x: x[0])
    ans = 0
    for i in range(n):
        if m <= 0:
            break
        a, b = arr[i]
        if m >= b:
            ans += a * b
            m -= b
        else:
            ans += a * m
            m = 0
    print(ans)

if __name__ == '__main__':
    main()