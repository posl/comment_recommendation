def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        si, ti = input().split()
        s.append(si)
        t.append(ti)
    for i in range(n):
        for j in range(n - 1):
            if s[j] == t[j + 1]:
                s[j], s[j + 1] = s[j + 1], s[j]
            if t[j] == s[j + 1]:
                t[j], t[j + 1] = t[j + 1], t[j]
    for i in range(n):
        if s[i] == t[i]:
            print('No')
            return
    print('Yes')
