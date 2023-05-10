def main():
    n,m = map(int,input().split())
    s = [input() for i in range(n)]
    t = [input() for i in range(m)]
    for i in range(n):
        for j in range(m):
            if s[i] == t[j]:
                print(-1)
                return
    for i in range(n):
        for j in range(m):
            if s[i] in t[j]:
                print(-1)
                return
    for i in range(n):
        for j in range(i+1,n):
            if s[i] == s[j]:
                print(-1)
                return
    for i in range(m):
        for j in range(i+1,m):
            if t[i] == t[j]:
                print(-1)
                return
    ans = ''
    for i in range(n):
        ans += s[i]
        if i < n-1:
            ans += '_'
    print(ans)
