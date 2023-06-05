def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    t = [input() for _ in range(h)]
    for i in range(h):
        s[i] = ''.join(sorted(s[i]))
        t[i] = ''.join(sorted(t[i]))
    for i in range(h):
        for j in range(w):
            if s[i][j] != t[i][j]:
                print('No')
                exit()
    print('Yes')
