def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [0] + a
    a.sort()
    print(a)
    ans = [0] * (n + 1)
    ans[0] = 0
    for i in range(1, n + 1):
        if a[i] != a[i - 1]:
            ans[i] = ans[i - 1] + 1
        else:
            ans[i] = ans[i - 1]
    print(ans)
    for i in range(1, n + 1):
        print(ans[i])

if __name__ == '__main__':
    main()