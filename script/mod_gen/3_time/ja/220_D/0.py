def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353
    ans = [0] * 10
    for i in range(10):
        cnt = 0
        for a in A:
            if a == i:
                cnt += 1
        ans[i] = pow(2, cnt - 1, mod)
    print(*ans, sep='
')

if __name__ == '__main__':
    main()