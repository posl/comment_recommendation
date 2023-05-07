def solve():
    s = input()
    n = len(s)
    ans = 0
    for i in range(n):
        ans += (ord(s[i])-ord('A')+1)*pow(26,n-i-1)
    print(ans)
