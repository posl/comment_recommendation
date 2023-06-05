def water_flower(h):
    #print(h)
    min_h = min(h)
    max_h = max(h)
    min_index = h.index(min_h)
    max_index = h.index(max_h)
    if min_h == max_h:
        return 0
    else:
        if min_index < max_index:
            for i in range(min_index,max_index):
                h[i] += 1
        else:
            for i in range(max_index,min_index):
                h[i] += 1
        return 1 + water_flower(h)
