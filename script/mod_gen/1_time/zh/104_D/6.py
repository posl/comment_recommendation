def main():
    s = input()
    q = 0
    for i in range(len(s)):
        if s[i] == "?":
            q += 1
    print (q)
    ans = 0
    for i in range(q+1):
        ans += 3**i
    print (ans)
    print (ans % (10**9 + 7))

if __name__ == '__main__':
    main()