def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = [0] * n
    for i in range(n - 1):
        if a[i] < a[i + 1]:
            ans[i + 1] = ans[i] + 1
        else:
            ans[i + 1] = ans[i]
    for i in range(n):
        print(ans[i])

if __name__ == '__main__':
    main()