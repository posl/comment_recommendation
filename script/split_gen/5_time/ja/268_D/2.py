def main():
    n,m = map(int, input().split())
    s = [input() for i in range(n)]
    t = [input() for i in range(m)]
    for i in range(m):
        if t[i] in s:
            print(-1)
            exit()
    for i in range(m):
        for j in range(n):
            if t[i] in s[j]:
                s[j] = s[j].replace(t[i], "_" * len(t[i]))
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if s[i] == s[j]:
                print(-1)
                exit()
    ans = ""
    for i in range(n):
        ans += s[i] + "_"
    print(ans[:-1])
