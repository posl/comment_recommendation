def main():
    n, k = map(int, input().split())
    sushis = []
    for _ in range(n):
        t, d = map(int, input().split())
        sushis.append((t, d))
    sushis.sort(key=lambda x: x[1], reverse=True)
    t_set = set()
    sushis_selected = []
    for t, d in sushis:
        if t not in t_set:
            t_set.add(t)
            sushis_selected.append((t, d))
    sushis_selected.sort(key=lambda x: x[1], reverse=True)
    ans = 0
    for t, d in sushis_selected[:k]:
        ans += d
    t_set = set()
    t_count = 0
    for t, d in sushis_selected[:k]:
        if t not in t_set:
            t_set.add(t)
            t_count += 1
    ans += t_count ** 2
    print(ans)
