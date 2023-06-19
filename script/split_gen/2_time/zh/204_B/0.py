def get_nuts(nuts):
    nuts.sort()
    nuts.reverse()
    nuts.pop(0)
    return sum(nuts)
