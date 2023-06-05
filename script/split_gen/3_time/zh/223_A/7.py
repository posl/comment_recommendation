def isPossible(x):
    for i in range(0, 15):
        for j in range(0, 15):
            if (i * 4 + j * 7) == x:
                return True
    return False
