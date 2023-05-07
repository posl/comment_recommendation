def main():
    n,m = map(int,input().split())
    s = []
    for i in range(n):
        s.append(input())
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(m):
                if s[i][k] == 'o' or s[j][k] == 'o':
                    ans += 1
                    break
    print(ans)
main()

if __name__ == '__main__':
    main()