def main():
    import sys
    readline = sys.stdin.buffer.readline
    mod = 10**9 + 7
    h,w = map(int,readline().split())
    s = [readline().rstrip().decode('utf-8') for _ in range(h)]
    t = [readline().rstrip().decode('utf-8') for _ in range(h)]
    s_cnt = [0]*w
    t_cnt = [0]*w
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                s_cnt[j] += 1
            if t[i][j] == '#':
                t_cnt[j] += 1
    s_cnt.sort()
    t_cnt.sort()
    for i in range(w):
        if s_cnt[i] != t_cnt[i]:
            print('No')
            exit()
    print('Yes')
