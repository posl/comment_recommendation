def main():
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n-1):
        ans |= a[i]
        ans ^= a[i]
    ans ^= a[-1]
    print(ans)

if __name__ == '__main__':
    main()