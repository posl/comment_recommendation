def get_nuts(nuts):
    nuts.sort(reverse=True)
    nuts = nuts[10:]
    return sum(nuts)
