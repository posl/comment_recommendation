def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = a[0]
    for i in range(1, n):
        if ans * 2 >= a[i]:
            ans += a[i]
        else:
            ans = a[i]
    print(ans)

if __name__ == '__main__':
    main()