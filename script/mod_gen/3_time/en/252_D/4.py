def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n-2):
        k = i+2
        for j in range(i+1, n-1):
            while k < n and a[i]+a[j] > a[k]:
                k += 1
            ans += k - j - 1
    print(ans)

if __name__ == '__main__':
    main()