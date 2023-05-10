def main():
    n, m = map(int, input().split())
    py = [list(map(int, input().split())) for _ in range(m)]
    py.sort(key=lambda x:x[1])
    
    cnt = [0] * (n + 1)
    for p, y in py:
        cnt[p] += 1
        print('{:06}{:06}'.format(p, cnt[p]))
