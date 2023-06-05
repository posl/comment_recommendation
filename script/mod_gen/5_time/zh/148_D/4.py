def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    if a[0] != 1:
        print(-1)
        return
    for i in range(n-1):
        if a[i] + 1 < a[i+1]:
            print(-1)
            return
    ans = 0
    for i in range(n-1):
        if a[i] + 1 == a[i+1]:
            ans += 1
    print(n - 1 - ans)

if __name__ == '__main__':
    main()