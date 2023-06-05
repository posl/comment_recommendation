def waterFlower(N, h):
    result = 0
    if N == 1:
        return h[0]
    for i in range(N-1):
        if h[i] < h[i+1]:
            result += h[i+1] - h[i]
    result += h[0]
    return result
