def main():
    r, x, y = map(int, input().split())
    distance = (x**2 + y**2)**(1/2)
    if distance%r == 0:
        print(int(distance//r))
    elif distance < r:
        print(2)
    else:
        print(int(distance//r)+1)
