def get_nuts(nuts):
    nuts = list(map(int, nuts.split()))
    nuts = [i-10 for i in nuts if i > 10]
    return sum(nuts)
