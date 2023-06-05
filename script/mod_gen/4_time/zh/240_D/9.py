def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * n
    for i in range(n):
        ans[i] = i + 1
    for i in range(n-1):
        if a[i] == a[i+1]:
            ans[i+1] = ans[i]
    for i in range(n-1, 0, -1):
        if a[i] == a[i-1]:
            ans[i-1] = ans[i]
    for i in range(n):
        print(ans[i])

if __name__ == '__main__':
    main()