def is_between(n):
    if -2**31 <= n <= 2**31-1:
        return "是"
    else:
        return "否"
