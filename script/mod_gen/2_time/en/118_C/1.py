def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-1, -1, -1):
        if a[i] <= ans:
            ans += 1
        else:
            ans += a[i] - ans
    print(ans)

if __name__ == '__main__':
    main()