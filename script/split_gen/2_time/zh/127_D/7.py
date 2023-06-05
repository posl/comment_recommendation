def main():
    n, m = map(int, input().split())
    l = []
    r = []
    for i in range(m):
        l_i, r_i = map(int, input().split())
        l.append(l_i)
        r.append(r_i)
    print(min(r) - max(l) + 1 if min(r) - max(l) >= 0 else 0)
