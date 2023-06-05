def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * 10
    for i in a:
        b[i] += 1
    ans = [0] * 10
    ans[0] = b[0] * (b[0] - 1) // 2 % 998244353
    for i in range(1, 10):
        ans[i] = b[0] * b[i] % 998244353
    for i in range(1, 5):
        ans[i * 2] += b[i] * (b[i] - 1) // 2 % 998244353
        ans[i * 2] %= 998244353
        for j in range(i + 1, 5):
            ans[i + j] += b[i] * b[j] * 2 % 998244353
            ans[i + j] %= 998244353
    for i in range(10):
        print(ans[i])

if __name__ == '__main__':
    main()