def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    t = [input() for _ in range(h)]
    s_count = [0 for _ in range(w)]
    t_count = [0 for _ in range(w)]
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                s_count[j] += 1
            if t[i][j] == '#':
                t_count[j] += 1
    if s_count == t_count:
        print('Yes')
    else:
        print('No')
