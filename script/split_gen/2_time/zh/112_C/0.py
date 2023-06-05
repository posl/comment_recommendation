def search(cost, time, i, t):
    if i == 0:
        return 0
    elif time[i] > t:
        return search(cost, time, i-1, t)
    else:
        return max(search(cost, time, i-1, t), search(cost, time, i-1, t-time[i])+cost[i])
