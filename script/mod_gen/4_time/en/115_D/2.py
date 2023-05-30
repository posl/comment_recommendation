def burger(level, layer):
    if level == 0:
        return 1
    elif layer == 1:
        return 0
    elif layer <= (2**(level+1) - 3):
        return burger(level-1, layer-1)
    elif layer == (2**(level+1) - 2):
        return (2**level - 1)
    elif layer <= (2**(level+1) - 1):
        return (2**level - 1) + burger(level-1, layer - (2**level))
level, layer = map(int, input().split())
print(burger(level, layer))
