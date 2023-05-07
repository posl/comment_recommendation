def rotation(x,y,d):
    import math
    r = math.radians(d)
    x2 = x * math.cos(r) - y * math.sin(r)
    y2 = x * math.sin(r) + y * math.cos(r)
    return x2, y2
a, b, d = map(int, input().split())
x2, y2 = rotation(a,b,d)
print(x2, y2)

if __name__ == '__main__':
    rotation()