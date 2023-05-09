def main():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(m)]
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
    for i in range(m):
        for j in range(m):
            if i == j:
                continue
            if t[i] == t[j]:
                print(-1)
                return
    for i in range(m):
        for j in range(n):
            if t[i] == s[j]:
                print(-1)
                return
    for i in range(n):
        for j in range(m):
            if s[i] == t[j]:
                print(-1)
                return
    for i in range(m):
        for j in range(m):
            if i == j:
                continue
            if t[i].replace('_', '') == t[j].replace('_', ''):
                print(-1)
                return
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if s[i].replace('_', '') == s[j].replace('_', ''):
                print(-1)
                return
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            for k in range(m):
                if t[k].replace('_', '') == s[i].replace('_', ''):
                    print(-1)
                    return
                if t[k].replace('_', '') == s[j].replace('_', ''):
                    print(-1)
                    return
    for i in range(m):
        for j in range(m):
            if i == j:
                continue
            for k in range(n):
                if s[k].replace('_', '') == t[i].replace('_', ''):
                    print(-1)
                    return
                if s[k].replace('_', '') == t[j].replace('_', ''):
                    print(-1)
                    return
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            for k in range(n):
