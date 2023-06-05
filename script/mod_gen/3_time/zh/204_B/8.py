def get_nuts(nuts):
    nuts.sort(reverse=True)
    nuts = nuts[10:]
    return sum(nuts)

if __name__ == '__main__':
    get_nuts()