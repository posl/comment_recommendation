def main():
    n, x = map(int, input().split())
    s = input()
    ans = x
    for i in s:
        if i == 'x':
            ans = max(0, ans - 1)
        else:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()