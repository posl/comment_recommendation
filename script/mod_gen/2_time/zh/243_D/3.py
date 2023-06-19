def main():
    n,x = map(int,input().split())
    s = input()
    #print(n,x,s)
    ans = x
    for i in range(n):
        if s[i] == 'L':
            ans -= 1
        elif s[i] == 'R':
            ans += 1
        else:
            ans = ans // 2
    print(ans)

if __name__ == '__main__':
    main()