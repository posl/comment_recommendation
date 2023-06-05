def find_kth_number(k, nums):
    if k == 1:
        return 1
    num = 1
    while k > 1:
        num += 1
        if num not in nums:
            k -= 1
    return num
