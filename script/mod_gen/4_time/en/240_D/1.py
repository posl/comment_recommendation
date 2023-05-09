def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (2 * 10 ** 5 + 1)
    for i in range(n):
        b[a[i]] += 1
    ans = 0
    for i in range(2 * 10 ** 5 + 1):
        ans += b[i] % 2
    print(ans)

if __name__ == '__main__':
    main()