def main():
    x, y, z = map(int, input().split())
    if y < 0:
        print(abs(x) + abs(y) + abs(z))
    else:
        print(-1)
