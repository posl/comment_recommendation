def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(30):
        b = [0] * n
        for j in range(n):
            b[j] = (a[j] >> i) & 1
        if sum(b) % 2 == 1:
            ans += 2 ** i
    print(ans)

if __name__ == '__main__':
    main()