def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 998244353
    count = [0] * 10
    for i in a:
        count[i] += 1
    ans = [0] * 10
    ans[0] = pow(2, count[0], mod) - 1
    for i in range(1, 10):
        ans[i] = pow(2, count[i], mod) * ans[0]
        ans[i] %= mod
    for i in range(1, n):
        ans[0] *= 2
        ans[0] %= mod
    print(*ans, sep="\n")

if __name__ == '__main__':
    main()