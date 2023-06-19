def main():
    n, m = map(int, input().split())
    s = []
    t = []
    for i in range(n):
        s.append(input())
    for i in range(m):
        t.append(input())
    s.sort(key=len)
    t.sort(key=len)
    for i in range(n):
        for j in range(m):
            if s[i] in t[j]:
                print(-1)
                return
    for i in range(m):
        for j in range(m):
            if i != j and t[i] in t[j]:
                print(-1)
                return
    for i in range(n):
        for j in range(n):
            if i != j and s[i] in s[j]:
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
        for j in range(n):
            if i != j:
                for k in range(m):
                    if s[i] + t[k] in s[j]:
                        print(-1)
                        return
                    if t[k] + s[i] in s[j]:
                        print(-1)
                        return
    for i in range(m):
        for j in range(m):
            if i != j:
                for k in range(n):
                    if t[i] + s[k] in t[j]:
                        print(-1)
                        return
                    if s[k] + t[i] in t[j]:
                        print(-1)
                        return
    for i in range(n):
        for j in range(n):
            if i != j:
                for k in range(m):
                    if s[i] + t[k] in t[j]:
                        print(-1)
                        return
                    if t[j] + s[i] in t[k]:
                        print(-1)
                        return
    for i in range(m):
        for j in range(m):
            if i != j:
                for k in range(n):
                    if t[i] + s[k] in s[j]:
                        print(-1)
                        return
                    if s[j] + t[i] in s[k]:
                        print(-1)
                        return
    for i
