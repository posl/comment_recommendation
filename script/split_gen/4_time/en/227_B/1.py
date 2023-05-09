def main():
    n = int(input())
    s = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if 4*s[i]*s[j]+3*s[i]+3*s[j] == s[k]:
                    ans += 1
    print(ans)
main()
1
