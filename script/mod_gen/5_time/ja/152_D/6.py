def main():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        if i % 10 == 0:
            continue
        s = str(i)
        if s[0] == s[-1]:
            ans += 1
    print(ans)
main()

if __name__ == '__main__':
    main()