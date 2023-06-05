def get_sum(start, end):
    if start == end:
        return start
    else:
        return (start + end) * (end - start + 1) // 2
