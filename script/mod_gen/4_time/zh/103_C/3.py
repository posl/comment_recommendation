def main():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    f = [0] * (10 ** 5 + 1)
    for i in range(N):
        for j in range(1, 10 ** 5 // a[i] + 1):
            f[a[i] * j] += 1
    ans = 0
    for i in range(10 ** 5 + 1):
        ans += f[i] * i
    print(ans)

if __name__ == '__main__':
    main()