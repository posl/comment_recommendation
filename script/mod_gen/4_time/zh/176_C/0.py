def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += abs(a[i] - a[n//2])
    print(ans)

if __name__ == '__main__':
    main()