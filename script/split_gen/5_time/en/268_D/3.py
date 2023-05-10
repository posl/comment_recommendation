def main():
    n,m = map(int, input().split())
    s = [input() for i in range(n)]
    t = [input() for i in range(m)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if s[i] == s[j]:
                print(-1)
                return
    for i in range(m):
        for j in range(m):
            if i == j:
                continue
            if t[i] == t[j]:
                print(-1)
                return
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
        for j in range(m):
            if t[j] in s[i]:
                print(-1)
                return
    for i in range(n):
        for j in range(m):
            if '_' in t[j]:
                t[j] = t[j].replace('_', '')
    for i in range(n):
        for j in range(m):
            if t[j] in s[i]:
                print(-1)
                return
    for i in range(n):
        for j in range(m):
            if s[i] in t[j]:
                print(-1)
                return
    for i in range(n):
        for j in range(m):
            if '_' in t[j]:
                t[j] = t[j].replace('_', '')
    for i in range(n):
        for j in range(m):
            if t[j] in s[i]:
                print(-1)
                return
    for i in range(n):
        for j in range(m):
            if s[i] in t[j]:
                print(-1)
                return
    for i in range(n):
        for j in range(m):
            if '_' in t[j]:
                t[j] = t[j].replace('_', '')
    for i in range(n):
        for j in range(m):
            if t[j] in s[i]:
                print(-1)
                return
    for i in range(n):
        for j in range(m):
            if s[i] in t[j]:
                print(-1)
                return
    for i in range(n):
