def main():
    n,m = map(int,input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    s.sort(key=len)
    t.sort(key=len)
    ans = []
    for i in range(n):
        for j in range(m):
            if t[j] in s[i]:
                ans.append(t[j])
    if len(ans) == 0:
        print(-1)
    else:
        print(ans[0])
main()
