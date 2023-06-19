def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if a[i] <= ans + 1:
            ans += a[i]
        else:
            break
    print(ans + 1)

if __name__ == '__main__':
    main()