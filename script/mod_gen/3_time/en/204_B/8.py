def nuts(nuts):
    result = 0
    for nut in nuts:
        if nut > 10:
            result += nut - 10
    return result

if __name__ == '__main__':
    nuts()