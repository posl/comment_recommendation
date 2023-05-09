def get_permutation(n, k):
    """
    :type n: int
    :type k: int
    :rtype: str
    """
    k = k - 1
    nums = [i for i in range(1, n + 1)]
    res = ''
    while n > 0:
        n -= 1
        index, k = divmod(k, math.factorial(n))
        res += str(nums[index])
        nums.remove(nums[index])
    return res

if __name__ == '__main__':
    get_permutation()