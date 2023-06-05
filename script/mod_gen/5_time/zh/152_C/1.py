def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    m = 0
    for i in range(n):
        if a[i] > m:
            ans += 1
            m = a[i]
    print(ans)

if __name__ == '__main__':
    main()