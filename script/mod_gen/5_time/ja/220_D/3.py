def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * 10
    ans[a[0]] = 1
    for i in range(1, n):
        new_ans = [0] * 10
        for j in range(10):
            new_ans[(j + a[i]) % 10] += ans[j]
            new_ans[(j * a[i]) % 10] += ans[j]
        ans = new_ans
    for i in range(10):
        print(ans[i] % 998244353)

if __name__ == '__main__':
    main()