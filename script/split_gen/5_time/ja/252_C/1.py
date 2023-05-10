def main():
    n = int(input())
    s = [input() for i in range(n)]
    ans = 0
    for i in range(1,n):
        ans += 10
        if s[i][0] == s[i-1][0]:
            ans -= 1
    print(ans)
main()
