def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * 10
    for i in range(10):
        ans[i] = a.count(i)
    for i in range(n - 1):
        ans2 = [0] * 10
        for j in range(10):
            ans2[(j + a[i]) % 10] += ans[j]
            ans2[(j * a[i]) % 10] += ans[j]
        ans = ans2
    for i in range(10):
        print(ans[i])

if __name__ == '__main__':
    main()