def main():
    s = input()
    t = input()
    ans = 0
    for i in range(len(t)):
        ans += 1 if t[i] != s[i] else 0
    print(ans)
main()
