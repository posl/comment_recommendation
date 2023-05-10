def rotate(a, b, d):
    import math
    rad = d * math.pi / 180
    a_ = a * math.cos(rad) - b * math.sin(rad)
    b_ = a * math.sin(rad) + b * math.cos(rad)
    return a_, b_
a, b, d = map(int, input().split())
a_, b_ = rotate(a, b, d)
print(a_, b_)

if __name__ == '__main__':
    rotate()