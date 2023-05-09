def main():
    x, y, z = map(int, input().split())
    if x < y < z:
        print(z - y + z - x)
    elif x > y > z:
        print(x - y + x - z)
    elif x < y > z:
        print(abs(x - z) + abs(y - z))
    else:
        print(-1)
