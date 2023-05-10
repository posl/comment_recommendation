def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    if r1 == r2 and c1 == c2:
        print(0)
        exit()
    if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1 - r2) + abs(c1 - c2) <= 3:
        print(1)
        exit()
    if (r1 + c1) % 2 == (r2 + c2) % 2:
        print(2)
        exit()
    for i in range(-3, 4):
        for j in range(-3, 4):
            x, y = r2 + i, c2 + j
            if x + y == r1 + c1 or x - y == r1 - c1:
                print(2)
                exit()
    print(3)
