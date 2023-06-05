def main():
    n,m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    s.sort(key=len)
    t.sort(key=len)
    for i in range(n):
        for j in range(m):
            if t[j] in s[i]:
                print(-1)
                return
    ans = s[0]
    for i in range(1,n):
        for j in range(len(ans)-len(s[i])+1):
            if ans[j:j+len(s[i])] == s[i]:
                break
            if j == len(ans)-len(s[i]):
                ans += s[i]
                break
    print(ans)
