def add_to_bag(bag, x):
    if len(bag) == 0:
        bag.append(x)
    else:
        bag.append(x + bag[-1])

if __name__ == '__main__':
    add_to_bag()