def main():
    x, y, z = map(int, input().split())
    if z >= 0:
        print(abs(x-y))
    else:
        print(-1)
