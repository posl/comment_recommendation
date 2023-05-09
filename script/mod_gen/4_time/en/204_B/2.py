def harvest_nuts(trees):
    nuts = 0
    for tree in trees:
        if tree > 10:
            nuts += tree - 10
    return nuts

if __name__ == '__main__':
    harvest_nuts()