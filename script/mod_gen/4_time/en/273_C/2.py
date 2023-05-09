def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    ans = [0] * n
    ans[0] = 1
    for i in range(1, n):
        if a[i] != a[i - 1]:
            ans[i] = ans[i - 1] + 1
        else:
            ans[i] = ans[i - 1]
    for i in range(n):
        print(ans[a.index(a[i])] - 1)

if __name__ == '__main__':
    main()