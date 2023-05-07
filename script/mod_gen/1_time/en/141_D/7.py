def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    
    a.sort(reverse=True)
    ans = 0
    
    for i in range(n):
        ans += a[i] // 2**m
        m -= 1
        if m < 0:
            ans += a[i]
    
    print(ans)
    
main()

if __name__ == '__main__':
    main()