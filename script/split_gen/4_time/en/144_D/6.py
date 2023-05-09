def main():
    import math
    a, b, x = map(int, input().split())
    if x < a**2*b/2:
        print(math.degrees(math.atan2(b, 2*x/a/b)))
    else:
        print(math.degrees(math.atan2(2/a*(b-x/a**2), a)))
