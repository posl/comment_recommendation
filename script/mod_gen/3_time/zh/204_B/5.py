def get_nuts(nuts):
    nuts_sum = 0
    for i in nuts:
        if i > 10:
            nuts_sum += i - 10
    return nuts_sum

if __name__ == '__main__':
    get_nuts()