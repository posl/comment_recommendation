def get_even_odd_pair_count(k):
    even_count = (k // 2) + (k % 2)
    odd_count = k // 2
    return even_count * odd_count
