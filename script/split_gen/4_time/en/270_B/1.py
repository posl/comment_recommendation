def main():
    x, y, z = map(int, input().split())
    if x > y:
        if y + z >= x:
            print(0)
        else:
            print(-1)
    else:
        if y - z <= x:
            print(0)
        else:
            print(-1)
