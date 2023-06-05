def get_sum(start, end):
    if start == end:
        return start
    else:
        return (start + end) * (end - start + 1) // 2

if __name__ == '__main__':
    get_sum()