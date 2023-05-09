def main():
    n, m = map(int, input().split())
    l = []
    r = []
    for i in range(m):
        l_i, r_i = map(int, input().split())
        l.append(l_i)
        r.append(r_i)
    l_max = max(l)
    r_min = min(r)
    if l_max <= r_min:
        print(r_min - l_max + 1)
    else:
        print(0)
