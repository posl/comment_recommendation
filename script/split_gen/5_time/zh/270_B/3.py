def solution(x, y, z):
    if y > 0 and z > 0:
        return -1
    elif y < 0 and z < 0:
        return -1
    else:
        return abs(y - z)
