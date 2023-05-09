def main():
    a, b, x = map(int, input().split())
    if x < a*a*b/2:
        h = 2*x/(a*b)
        print(math.degrees(math.atan2(b-h, a)))
    else:
        h = 2*(a*a*b-x)/(a*a)
        print(math.degrees(math.atan2(b-h, a)))
