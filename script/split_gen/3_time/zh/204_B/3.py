def getNutsCount(nuts):
    nutsCount = 0
    for nut in nuts:
        if nut > 10:
            nutsCount += nut - 10
    return nutsCount
