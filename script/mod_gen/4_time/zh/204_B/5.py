def get_nuts(nuts):
    total = 0
    for nut in nuts:
        if nut > 10:
            total += nut - 10
    return total

if __name__ == '__main__':
    get_nuts()