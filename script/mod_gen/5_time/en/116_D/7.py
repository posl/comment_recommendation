def solve(N, K, sushi):
    # sort by deliciousness
    sushi.sort(key=lambda x: x[1], reverse=True)
    # sort by type
    sushi.sort(key=lambda x: x[0])
    # print(sushi)
    # pick up the top K sushi
    picked = sushi[:K]
    # print(picked)
    # count the number of types
    types = {}
    for t, d in picked:
        if t in types:
            types[t] += 1
        else:
            types[t] = 1
    # print(types)
    # calculate the satisfaction
    satisfaction = 0
    for t, d in picked:
        satisfaction += d
    satisfaction += len(types) ** 2
    # print(satisfaction)
    # calculate the maximum satisfaction
    max_satisfaction = satisfaction
    for i in range(K, N):
        # print("i:", i)
        # print("picked:", picked)
        # print("types:", types)
        # pick up the next sushi
        t, d = sushi[i]
        # print("next sushi:", t, d)
        # remove the last sushi
        t_last, d_last = picked.pop()
        # print("last sushi:", t_last, d_last)
        satisfaction -= d_last
        types[t_last] -= 1
        if types[t_last] == 0:
            types.pop(t_last)
        satisfaction -= len(types) ** 2
        # print("satisfaction:", satisfaction)
        # add the next sushi
        picked.append((t, d))
        satisfaction += d
        if t in types:
            types[t] += 1
        else:
            types[t] = 1
        satisfaction += len(types) ** 2
        # print("satisfaction:", satisfaction)
        # update the maximum satisfaction
        max_satisfaction = max(max_satisfaction, satisfaction)
        # print("max_satisfaction:", max_satisfaction)
    return max_satisfaction

if __name__ == '__main__':
    solve()