def bitSum(x, y):
    result = 0
    while x>0 or y>0:
        result += (x%2)*(y%2)
        x //= 2
        y //= 2
    return result
