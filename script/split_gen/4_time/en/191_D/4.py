def main():
    import math
    x, y, r = map(float, input().split())
    x = math.floor(x*10000)
    y = math.floor(y*10000)
    r = math.floor(r*10000)
    count = 0
    for i in range(x-r, x+r+1):
        j = math.floor(math.sqrt(r**2 - (i-x)**2))
        count += math.floor((y+j)/10000) - math.floor((y-j)/10000) + 1
    print(count)
