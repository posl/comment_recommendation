def rotate(x, y, d):
    import math
    rad = math.radians(d)
    return x * math.cos(rad) - y * math.sin(rad), x * math.sin(rad) + y * math.cos(rad)
x, y, d = map(int, input().split())
x, y = rotate(x, y, d)
print(x, y)

if __name__ == '__main__':
    rotate()