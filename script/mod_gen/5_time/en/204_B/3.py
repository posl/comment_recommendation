def harvest_nuts(nuts):
    total_nuts = 0
    for nut in nuts:
        if nut > 10:
            total_nuts += nut - 10
    return total_nuts

if __name__ == '__main__':
    harvest_nuts()