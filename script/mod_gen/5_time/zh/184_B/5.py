def main():
    n,x = map(int,input().split())
    s = input()
    ans = x
    for i in range(n):
        if s[i] == 'x':
            if ans > 0:
                ans -= 1
        else:
            ans += 1
    print(ans)
main()
