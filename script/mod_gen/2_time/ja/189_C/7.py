def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = 0
    for i in range(1, n):
        if a[i] < a[i-1]:
            ans += a[i-1]-a[i]
            a[i] = a[i-1]
    print(ans)

if __name__ == '__main__':
    main()