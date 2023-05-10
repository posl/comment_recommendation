def get_max_satisfaction(N, K, sushi):
    # sort sushi by deliciousness
    sushi.sort(key=lambda x: x[1], reverse=True)
    # get the number of each type of sushi
    sushi_count = {}
    for i in range(N):
        if sushi[i][0] not in sushi_count:
            sushi_count[sushi[i][0]] = 1
        else:
            sushi_count[sushi[i][0]] += 1
    # get the number of each type of sushi in the top K sushi
    sushi_count_top = {}
    for i in range(K):
        if sushi[i][0] not in sushi_count_top:
            sushi_count_top[sushi[i][0]] = 1
        else:
            sushi_count_top[sushi[i][0]] += 1
    # get the number of each type of sushi in the top K sushi
    # and not in the top K sushi
    sushi_count_top_and_not = {}
    sushi_count_not_top = {}
    for i in range(N):
        if i < K:
            if sushi[i][0] not in sushi_count_top_and_not:
                sushi_count_top_and_not[sushi[i][0]] = 1
            else:
                sushi_count_top_and_not[sushi[i][0]] += 1
        else:
            if sushi[i][0] not in sushi_count_not_top:
                sushi_count_not_top[sushi[i][0]] = 1
            else:
                sushi_count_not_top[sushi[i][0]] += 1
    # get the number of each type of sushi in the top K sushi
    # and not in the top K sushi
    # and in the top K sushi and not in the top K sushi
    sushi_count_top_and_not_and_not_top = {}
    for i in range(N):
        if i < K:
            if sushi[i][0] not in sushi_count_top_and_not_and_not_top:
                sushi_count_top_and_not_and_not_top[sushi[i][0]] = 1
            else:
                sushi_count_top_and_not_and_not_top[sushi[i][0]] += 1
        else:
            if sushi[i][0] not in sushi_count_top_and_not_and_not_top:
                sushi_count_top_and_not_and_not_top[sushi[i][0]] = 0
    # get the number of each type of sushi in the

if __name__ == '__main__':
    get_max_satisfaction()