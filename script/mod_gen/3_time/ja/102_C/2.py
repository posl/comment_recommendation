def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += abs(a[n//2] - a[i])
    print(ans)

if __name__ == '__main__':
    main()