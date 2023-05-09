def main():
    R, X, Y = map(int, input().split())
    distance = (X ** 2 + Y ** 2) ** 0.5
    steps = (distance / R)
    if steps.is_integer():
        print(int(steps))
    else:
        print(int(steps) + 1)
