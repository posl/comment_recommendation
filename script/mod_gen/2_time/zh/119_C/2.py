def main():
    n = int(input())
    ans = 0
    for i in range(n):
        x, u = input().split()
        if u == 'JPY':
            ans += float(x)
        else:
            ans += float(x) * 380000
    print(ans)

if __name__ == '__main__':
    main()