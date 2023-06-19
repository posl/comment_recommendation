def get_nuts(nuts):
    nuts = [int(nut) for nut in nuts.split(' ')]
    nuts.sort()
    nuts.reverse()
    nuts = [nut - 10 for nut in nuts]
    nuts = [nut if nut > 0 else 0 for nut in nuts]
    return sum(nuts)

if __name__ == '__main__':
    get_nuts()