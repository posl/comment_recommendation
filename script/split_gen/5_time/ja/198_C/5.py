def main():
    r, x, y = map(int, input().split())
    d = (x**2 + y**2)**(1/2)
    if d < r:
        print(2)
    else:
        print(int(d//r) + int(d%r > 0))
