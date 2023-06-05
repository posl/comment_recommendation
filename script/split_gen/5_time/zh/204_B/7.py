def harvest_nuts(nuts):
    nuts = [int(nut) for nut in nuts]
    nuts.sort(reverse=True)
    nuts = [nut if nut < 10 else nut - 10 for nut in nuts]
    return sum(nuts)
