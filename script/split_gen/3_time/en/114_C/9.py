def is_shichigosan(n):
    digits = [int(d) for d in str(n)]
    return (7 in digits) and (5 in digits) and (3 in digits) and (set(digits) <= {7, 5, 3})
