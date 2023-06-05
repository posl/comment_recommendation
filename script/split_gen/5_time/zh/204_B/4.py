def get_nuts(nuts):
    nuts = list(map(int, nuts.split()))
    nuts.sort(reverse=True)
    nuts = list(filter(lambda x: x >= 10, nuts))
    nuts = list(map(lambda x: x - 10, nuts))
    return sum(nuts)
