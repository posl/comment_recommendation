def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for bit in range(1 << n):
        count = 0
        sum = 0
        for i in range(n):
            if bit & (1 << i):
                count += 1
                sum += a[i]
        if sum % count == 0:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()