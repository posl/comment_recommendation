def getNutsFromTree(nuts):
    nuts.sort(reverse=True)
    nuts.pop(0)
    return sum(nuts)
