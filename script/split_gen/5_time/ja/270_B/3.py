def main():
    x, y, z = map(int, input().split())
    if x < y:
        if y < z:
            print(-1)
        else:
            print(y-x)
    else:
        if z < y:
            print(-1)
        else:
            print(z-x)
