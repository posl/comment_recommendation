def main():
    n = int(input())
    v = list(map(int, input().split()))
    even, odd = v[::2], v[1::2]
    even_cnt = dict()
    odd_cnt = dict()
    for i in range(n//2):
        even_cnt[even[i]] = even_cnt.get(even[i], 0) + 1
        odd_cnt[odd[i]] = odd_cnt.get(odd[i], 0) + 1
    even_cnt = sorted(even_cnt.items(), key=lambda x:x[1], reverse=True)
    odd_cnt = sorted(odd_cnt.items(), key=lambda x:x[1], reverse=True)
    if even_cnt[0][0] != odd_cnt[0][0]:
        print(n - even_cnt[0][1] - odd_cnt[0][1])
    else:
        if len(even_cnt) == 1 and len(odd_cnt) == 1:
            print(n//2)
        elif len(even_cnt) == 1:
            print(n//2 - odd_cnt[1][1])
        elif len(odd_cnt) == 1:
            print(n//2 - even_cnt[1][1])
        else:
            print(min(n - even_cnt[0][1] - odd_cnt[1][1], n - even_cnt[1][1] - odd_cnt[0][1]))

if __name__ == '__main__':
    main()