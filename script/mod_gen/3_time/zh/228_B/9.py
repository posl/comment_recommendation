def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] -= 1
    b = [0] * n
    b[x - 1] = 1
    for i in range(n):
        b[a[i]] += 1
    ans = 0
    for i in range(n):
        if b[i] > 1:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()