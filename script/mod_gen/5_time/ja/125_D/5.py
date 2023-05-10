def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        ans += abs(a[i] - a[i+1])
    ans += abs(a[0])
    ans += abs(a[n-1])
    for i in range(n-1):
        if i == 0:
            print(ans - abs(a[i]) - abs(a[i] - a[i+1]) + abs(a[i+1]))
        elif i == n-2:
            print(ans - abs(a[i] - a[i+1]) - abs(a[i+1]) + abs(a[i]))
        else:
            print(ans - abs(a[i] - a[i+1]) - abs(a[i+1]) - abs(a[i] - a[i-1]) + abs(a[i+1] - a[i-1]))

if __name__ == '__main__':
    main()