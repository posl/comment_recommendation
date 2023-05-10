def resolve():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    t = [input() for _ in range(h)]
    s = ["".join(sorted(s[i])) for i in range(h)]
    t = ["".join(sorted(t[i])) for i in range(h)]
    s.sort()
    t.sort()
    if s == t:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    resolve()