def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    ans = [0] * n
    for i in range(n):
        ans[i] = t[i]
        if i > 0 and ans[i] <= ans[i - 1]:
            ans[i] = ans[i - 1] + 1
        if i < n - 1 and s[i] + ans[i] <= ans[i + 1]:
            ans[i] = ans[i + 1] - s[i]
    for i in range(n):
        print(ans[i])

if __name__ == '__main__':
    main()