def get_good_nums(N, W, A):
    A.sort()
    A.reverse()
    max_a = A[0]
    if max_a >= W:
        return W
    good_nums = [0] * (W+1)
    good_nums[0] = 1
    for i in range(N):
        for j in range(W+1):
            if good_nums[j] == 1:
                if j + A[i] <= W:
                    good_nums[j+A[i]] = 1
    return sum(good_nums)
