def main():
    n = int(input())
    ans = 0
    for i in range(1,n+1):
        s = str(i)
        if s[0] == s[-1]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()