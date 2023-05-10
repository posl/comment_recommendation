def main():
    n = int(input())
    v = list(map(int, input().split()))
    odd = []
    even = []
    for i in range(n):
        if i % 2 == 0:
            even.append(v[i])
        else:
            odd.append(v[i])
    from collections import Counter
    even_cnt = Counter(even).most_common()
    odd_cnt = Counter(odd).most_common()
    if even_cnt[0][0] != odd_cnt[0][0]:
        print(n - even_cnt[0][1] - odd_cnt[0][1])
    elif len(even_cnt) == 1 and len(odd_cnt) == 1:
        print(n // 2)
    elif len(even_cnt) == 1:
        print(n // 2 - odd_cnt[1][1])
    elif len(odd_cnt) == 1:
        print(n // 2 - even_cnt[1][1])
    else:
        print(min(n - even_cnt[0][1] - odd_cnt[1][1], n - even_cnt[1][1] - odd_cnt[0][1]))
