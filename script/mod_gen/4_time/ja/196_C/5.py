def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        s = str(i)
        if len(s) % 2 == 0 and s[0:len(s)//2] == s[len(s)//2:]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()