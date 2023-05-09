def main():
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    r1 -= r2
    c1 -= c2
    if r1 == c1 == 0:
        print(0)
        return
    if r1 == c1 or r1 == -c1 or abs(r1) + abs(c1) <= 3:
        print(1)
        return
    if (r1 + c1) % 2 == 0 or abs(r1) + abs(c1) <= 6 or abs(r1 - c1) <= 3 or abs(r1 + c1) <= 3:
        print(2)
        return
    print(3)
