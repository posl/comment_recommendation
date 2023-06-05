def get_max_product(n):
    if n <= 10:
        return n
    else:
        s = str(n)
        length = len(s)
        if length % 2 == 0:
            half = length // 2
            return int(s[:half]) * int(s[half:])
        else:
            half = length // 2
            return max(int(s[:half]) * int(s[half:]), int(s[:half+1]) * int(s[half+1:]))
