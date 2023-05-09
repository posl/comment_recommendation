def getNumPatties(N, X):
    if N == 0:
        return 0
    elif N == 1:
        return 1 if X > 1 else 0
    else:
        totalLayers = 3 + getNumLayers(N - 1) * 2
        if X > totalLayers:
            return getNumPatties(N - 1, X - 2) + 2 ** (N - 1)
        elif X > 2:
            return getNumPatties(N - 1, X - 1)
        else:
            return 0
