def main():
    n, k = map(int, input().split())
    s = input()
    s = list(s)
    s.append(' ')
    #print(s)
    ans = 0
    for i in range(n):
        if s[i] == s[i+1]:
            ans += 1
    ans += 2 * min(k, ans)
    print(ans)

if __name__ == '__main__':
    main()