def main():
    x, y, z = map(int, input().split())
    if x < y and x < z:
        print(-1)
    else:
        print(abs(y - z) + x)
