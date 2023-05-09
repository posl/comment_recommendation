def main():
    n, l = map(int, input().split())
    ans = 0
    for i in range(1, n+1):
        ans += l+i-1
    if l > 0:
        ans -= l
    elif l+n-1 < 0:
        ans -= l+n-1
    print(ans)

if __name__ == '__main__':
    main()