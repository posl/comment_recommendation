def main():
    n, k = map(int, input().split())
    sushi = [list(map(int, input().split())) for _ in range(n)]
    sushi.sort(key=lambda x: x[1], reverse=True)
    sushi.sort(key=lambda x: x[0])
    # print(sushi)
    sushi_dict = {}
    for t, d in sushi:
        if t not in sushi_dict:
            sushi_dict[t] = []
        sushi_dict[t].append(d)
    # print(sushi_dict)
    sushi_list = []
    for t, d in sushi_dict.items():
        sushi_list.append([t, sum(d)])
    # print(sushi_list)
    sushi_list.sort(key=lambda x: x[1], reverse=True)
    # print(sushi_list)
    sushi_list = sushi_list[:k]
    # print(sushi_list)
    sushi_list.sort(key=lambda x: x[0])
    # print(sushi_list)
    sushi_list = sushi_list[::-1]
    # print(sushi_list)
    sushi_dict = {}
    for t, d in sushi_list:
        if t not in sushi_dict:
            sushi_dict[t] = []
        sushi_dict[t].append(d)
    # print(sushi_dict)
    sushi_list = []
    for t, d in sushi_dict.items():
        sushi_list.append([t, len(d)])
    # print(sushi_list)
    ans = 0
    for t, d in sushi_list:
        ans += d ** 2
    # print(ans)
    for t, d in sushi_list:
        ans += sum(sushi_dict[t])
    print(ans)

if __name__ == '__main__':
    main()