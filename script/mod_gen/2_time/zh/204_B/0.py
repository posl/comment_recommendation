def get_nuts(nuts):
    nuts.sort()
    nuts.reverse()
    nuts.pop(0)
    return sum(nuts)

if __name__ == '__main__':
    get_nuts()