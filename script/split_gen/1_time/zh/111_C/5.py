def solve(n, v):
    odd = v[::2]
    even = v[1::2]
    from collections import Counter
    odd_cnt = Counter(odd).most_common()
    even_cnt = Counter(even).most_common()
    if len(odd_cnt) == 1 and len(even_cnt) == 1:
        if odd_cnt[0][0] == even_cnt[0][0]:
            return n // 2
        else:
            return 0
    if len(odd_cnt) == 1:
        return n // 2 - even_cnt[0][1]
    if len(even_cnt) == 1:
        return n // 2 - odd_cnt[0][1]
    return n - odd_cnt[0][1] - even_cnt[0][1]
