def main():
    a,b,d = map(int, input().split())
    theta = math.radians(d)
    x = a * math.cos(theta) - b * math.sin(theta)
    y = a * math.sin(theta) + b * math.cos(theta)
    print(x,y)
