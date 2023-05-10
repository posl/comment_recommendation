def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a[x-1] = 0
    ans = 1
    for i in a:
        if i != 0:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()