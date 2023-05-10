def main():
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    ans = -1
    for i in range(n-k+1):
        if a[i]%d == 0:
            ans = a[i]
            break
    print(ans)

if __name__ == '__main__':
    main()