def main():
    r1, c1 = map(int, input().split()) # r1, c1
    r2, c2 = map(int, input().split()) # r2, c2
    if r1 == r2 and c1 == c2:
        print(0)
    elif r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
    elif (r1 + c1) % 2 == (r2 + c2) % 2 or abs(r1 - r2) + abs(c1 - c2) <= 6:
        print(2)
    else:
        print(3)
