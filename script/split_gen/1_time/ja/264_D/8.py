def main():
    s = list(input())
    t = "atcoder"
    ans = 0
    for i in range(len(s)):
        if (s[i] != t[i]):
            ans += len(s) - i
            break
    print(ans)
main()
