def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, n):
        ans += (a[i] - a[i-1])**2
    for i in range(1, n-1):
        ans -= 2*(a[i] - a[i-1])*(a[i+1] - a[i])
    print(ans)

if __name__ == '__main__':
    main()