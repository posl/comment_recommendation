def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(0,0)
    ans = 0
    for i in range(1,k+1):
        if a[i] > n:
            break
        else:
            ans += n // a[i]
            n = n % a[i]
    print(ans)

if __name__ == '__main__':
    main()