def main():
    n, x = map(int, input().split())
    s = input()
    ans = 0
    for i in range(n):
        if s[i] == "o":
            ans += 1
        else:
            if ans > 0:
                ans -= 1
    print(x+ans)

if __name__ == '__main__':
    main()