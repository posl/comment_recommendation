def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = a[::-1]
    ans = 0
    for i in range(1, n):
        if a[i] > a[i-1]:
            ans += a[i] - a[i-1]
            a[i] = a[i-1]
    print(ans)
main()
