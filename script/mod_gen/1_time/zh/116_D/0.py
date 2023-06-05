def main():
    n,k = map(int, input().split())
    sushi = [list(map(int, input().split())) for _ in range(n)]
    sushi.sort(key=lambda x: x[1], reverse=True)
    type_cnt = {}
    type_list = []
    for t, d in sushi[:k]:
        if t not in type_cnt:
            type_cnt[t] = 0
            type_list.append(t)
        type_cnt[t] += 1
    type_list.sort()
    type_cnt_list = [type_cnt[t] for t in type_list]
    type_cnt_list.sort(reverse=True)
    t

if __name__ == '__main__':
    main()