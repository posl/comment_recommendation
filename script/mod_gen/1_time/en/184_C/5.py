def ryuma(r1,c1,r2,c2):
    if r1 == r2 and c1 == c2:
        return 0
    if r1 + c1 == r2 + c2:
        return 1
    if r1 - c1 == r2 - c2:
        return 1
    if abs(r1 - r2) + abs(c1 - c2) <= 3:
        return 1
    if (r1 + c1) % 2 == (r2 + c2) % 2:
        return 2
    if abs((r1 + c1) - (r2 + c2)) <= 3:
        return 2
    if abs((r1 - c1) - (r2 - c2)) <= 3:
        return 2
    return 3
r1,c1 = map(int,input().split())
r2,c2 = map(int,input().split())
print(ryuma(r1,c1,r2,c2))

if __name__ == '__main__':
    ryuma()