def main():
    a,b = map(int,input().split())
    x = 1
    y = 0
    while True:
        if x**2 + y**2 > a**2 + b**2:
            break
        x += 1
        y += 1
    x -= 1
    y -= 1
    if x == 0:
        x = 1
    print((x*a)/((x**2+y**2)**0.5),(y*b)/((x**2+y**2)**0.5))
