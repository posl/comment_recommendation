def waterFlowers(flowers):
    if len(flowers) == 0:
        return 0
    if len(flowers) == 1:
        return flowers[0]
    if len(flowers) == 2:
        return max(flowers)
    if len(flowers) == 3:
        return max(flowers[0] + flowers[2], flowers[1])
    if len(flowers) == 4:
        return max(flowers[0] + flowers[2], flowers[1] + flowers[3])
    if len(flowers) == 5:
        return max(flowers[0] + flowers[2] + flowers[4], flowers[1] + flowers[3])
    return max(flowers[0] + waterFlowers(flowers[2:]), flowers[1] + waterFlowers(flowers[3:]))
