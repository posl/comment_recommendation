def main():
    a, b, x = map(int, input().split())
    if x <= a**2*b/2:
        ans = math.degrees(math.atan((2*x)/(a*b**2)))
    else:
        ans = math.degrees(math.atan((a*b**2-2*x)/(a**2*b)))
    print(ans)
