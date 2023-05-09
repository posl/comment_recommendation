def main():
    r, x, y = map(int, input().split())
    distance = (x**2 + y**2)**(1/2)
    if distance == r:
        print(1)
    elif distance <= 2*r:
        print(2)
    else:
        print(int(distance//r) + (distance%r != 0))
