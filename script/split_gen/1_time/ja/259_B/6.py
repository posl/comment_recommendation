def main():
    import math
    a,b,d = map(int,input().split())
    rad = math.radians(d)
    print(a*math.cos(rad) - b*math.sin(rad),a*math.sin(rad) + b*math.cos(rad))
