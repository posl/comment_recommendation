def main():
    import math
    a,b,d = map(int, input().split())
    rad = math.radians(d)
    cos = math.cos(rad)
    sin = math.sin(rad)
    x = a * cos - b * sin
    y = a * sin + b * cos
    print(x,y)
