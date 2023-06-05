def find_best_route(N, T, c_list, t_list):
    best_cost = 1001
    for i in range(N):
        if t_list[i] <= T and c_list[i] < best_cost:
            best_cost = c_list[i]
    if best_cost == 1001:
        print("TLE")
    else:
        print(best_cost)
