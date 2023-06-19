def problem259_b():
    a,b,d = input().split(' ')
    a = float(a)
    b = float(b)
    d = float(d)
    import math
    d = math.radians(d)
    a1 = a * math.cos(d) - b * math.sin(d)
    b1 = a * math.sin(d) + b * math.cos(d)
    print('{0:.20f} {1:.20f}'.format(a1,b1))
