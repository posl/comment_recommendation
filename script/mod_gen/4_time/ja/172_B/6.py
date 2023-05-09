def main():
    s = input()
    t = input()
    n = len(s)
    ans = n
    for i in range(n):
        if s[i:] + s[:i] == t:
            ans = min(ans, i)
    print(ans)
main()

if __name__ == '__main__':
    main()