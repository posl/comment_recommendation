def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * 10
    for k in range(10):
        for i in range(n):
            if a[i] == k:
                if i % 2 == 0:
                    ans[k] += 1
                else:
                    ans[k] += 998244353 - 1
    for k in range(10):
        print(ans[k] % 998244353)

if __name__ == '__main__':
    main()