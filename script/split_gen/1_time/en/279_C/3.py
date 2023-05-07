def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    t = [input() for _ in range(h)]
    ss = []
    tt = []
    for i in range(h):
        ss.append(sorted(s[i]))
        tt.append(sorted(t[i]))
    ss.sort()
    tt.sort()
    for i in range(h):
        if ss[i] != tt[i]:
            print('No')
            return
    print('Yes')
    return
