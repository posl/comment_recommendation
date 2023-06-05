def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
    #print(s)
    #print(t)
    #print(len(s))
    #print(len(t))
    #print(s[0])
    #print(t[0])
    #print(s[0][-3:])
    #print(t[0])
    #print(s[0][-3:] == t[0])
    ans = 0
    for i in range(n):
        for j in range(m):
            if s[i][-3:] == t[j]:
                ans += 1
    print(ans)
