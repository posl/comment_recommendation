def main():
    n, m = map(int, input().split())
    s = [input() for i in range(n)]
    t = [input() for i in range(m)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            for k in range(m):
                if t[k] == s[i] + '_' + s[j]:
                    print(t[k])
                    return
                if t[k] == s[j] + '_' + s[i]:
                    print(t[k])
                    return
    print(-1)
main()
