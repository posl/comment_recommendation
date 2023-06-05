def main():
    n,k = map(int,input().split())
    s = list(map(int,input()))
    ans = 0
    for i in range(n):
        if s[i] == 0:
            ans += 1
    tmp = ans
    for i in range(k):
        if s[i] == 0:
            tmp += 1
        else:
            tmp -= 1
        ans = max(ans,tmp)
    print(ans)

if __name__ == '__main__':
    main()