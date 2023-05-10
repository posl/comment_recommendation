def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        if a[i] < 0:
            ans += abs(a[i])
            a[i] = 0
        if a[i+1] < 0:
            ans += abs(a[i+1])
            a[i+1] = 0
    print(ans + sum(a))

if __name__ == '__main__':
    main()