def find_max_village(N, K, AB):
    AB.sort(key=lambda x: x[0])
    AB.sort(key=lambda x: x[1], reverse=True)
    # print(AB)
    res = 0
    for i in range(N):
        if K >= AB[i][0]:
            K += AB[i][1]
            res = AB[i][0]
    return res
