def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 1
    for i in range(n):
        if ans < a[i]:
            print(ans)
            exit()
        ans += a[i]
    print(ans)

if __name__ == '__main__':
    main()