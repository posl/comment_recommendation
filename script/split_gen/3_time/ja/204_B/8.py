def harvest(trees):
    result = 0
    for tree in trees:
        if tree > 10:
            result += tree - 10
    return result
