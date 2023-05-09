def main():
    import math
    x, y, r = map(float, input().split())
    x, y = x*10000, y*10000
    r = r*10000
    x1 = math.ceil(x-r)
    x2 = math.floor(x+r)
    count = 0
    for i in range(x1, x2+1):
        y1 = math.ceil(y-math.sqrt(r**2-(x-i)**2))
        y2 = math.floor(y+math.sqrt(r**2-(x-i)**2))
        count += y2-y1+1
    print(count)
