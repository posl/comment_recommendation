def main():
    n = int(input())
    v = list(map(int, input().split()))
    even = v[0::2]
    odd = v[1::2]
    even_cnt = {}
    odd_cnt = {}
    for i in range(n//2):
        even_cnt[even[i]] = even_cnt.get(even[i], 0) + 1
        odd_cnt[odd[i]] = odd_cnt.get(odd[i], 0) + 1
    even_cnt_sorted = sorted(even_cnt.items(), key=lambda x: x[1], reverse=True)
    odd_cnt_sorted = sorted(odd_cnt.items(), key=lambda x: x[1], reverse=True)
    if even_cnt_sorted[0][0] == odd_cnt_sorted[0][0]:
        if len(even_cnt_sorted) == 1 and len(odd_cnt_sorted) == 1:
            print(n//2)
        elif len(even_cnt_sorted) == 1:
            print(n//2 - odd_cnt_sorted[1][1])
        elif len(odd_cnt_sorted) == 1:
            print(n//2 - even_cnt_sorted[1][1])
        else:
            print(min(n//2 - even_cnt_sorted[1][1] - odd_cnt_sorted[0][1], n//2 - even_cnt_sorted[0][1] - odd_cnt_sorted[1][1]))
    else:
        print(n//2 - even_cnt_sorted[0][1] - odd_cnt_sorted[0][1])
