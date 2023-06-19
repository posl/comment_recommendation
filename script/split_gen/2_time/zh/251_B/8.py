def get_good_num(n,w,weights):
    weights.sort()
    good_nums = [False for i in range(w+1)]
    good_nums[0] = True
    for weight in weights:
        for i in range(w,-1,-1):
            if i - weight >= 0 and good_nums[i-weight]:
                good_nums[i] = True
    return sum(good_nums)
