def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(1, n):
        if a[i] != a[i-1]:
            ans += i
    print(ans)
main()

if __name__ == '__main__':
    main()